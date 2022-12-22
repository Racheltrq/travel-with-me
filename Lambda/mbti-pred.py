# This file lives in an Amazon ECR container.
import json
import time
import re
import pandas as pd
import tempfile
import nltk
import boto3
from io import StringIO
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.data.path.append("/tmp")
nltk.download('punkt', download_dir="/tmp")
nltk.download('averaged_perceptron_tagger', download_dir="/tmp")
nltk.download('wordnet', download_dir="/tmp")
nltk.download('stopwords', download_dir="/tmp")
nltk.download('omw-1.4', download_dir="/tmp")
s3_client = boto3.client('s3')
bucket_name = "travelwithme-mbti-models"

# sentiment scoring
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# importing model
from joblib import load

mbti = [
    "INFP",
    "INFJ",
    "INTP",
    "INTJ",
    "ENTP",
    "enfp",
    "ISTP",
    "ISFP",
    "ENTJ",
    "ISTJ",
    "ENFJ",
    "ISFJ",
    "ESTP",
    "ESFP",
    "ESFJ",
    "ESTJ",
]
tags_dict = {
    "ADJ_avg": ["JJ", "JJR", "JJS"],
    "ADP_avg": ["EX", "TO"],
    "ADV_avg": ["RB", "RBR", "RBS", "WRB"],
    "CONJ_avg": ["CC", "IN"],
    "DET_avg": ["DT", "PDT", "WDT"],
    "NOUN_avg": ["NN", "NNS", "NNP", "NNPS"],
    "NUM_avg": ["CD"],
    "PRT_avg": ["RP"],
    "PRON_avg": ["PRP", "PRP$", "WP", "WP$"],
    "VERB_avg": ["MD", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
    ".": ["#", "$", "''", "(", ")", ",", ".", ":"],
    "X": ["FW", "LS", "UH"],
}
features = [
    "clean_posts",
    "compound_sentiment",
    "ADJ_avg",
    "ADP_avg",
    "ADV_avg",
    "CONJ_avg",
    "DET_avg",
    "NOUN_avg",
    "NUM_avg",
    "PRT_avg",
    "PRON_avg",
    "VERB_avg",
    "qm",
    "em",
    "colons",
    "emojis",
    "word_count",
    "unique_words",
    "upper",
    "link_count",
    "ellipses",
    "img_count",
]


def unique_words(s):
    unique = set(s.split(" "))
    return len(unique)


def emojis(post):
    # does not include emojis made purely from symbols, only :word:
    emoji_count = 0
    words = post.split()
    for e in words:
        if "http" not in e:
            if e.count(":") == 2:
                emoji_count += 1
    return emoji_count


def colons(post):
    # Includes colons used in emojis
    colon_count = 0
    words = post.split()
    for e in words:
        if "http" not in e:
            colon_count += e.count(":")
    return colon_count


def lemmitize(s):
    lemmatizer = WordNetLemmatizer()
    new_s = ""
    for word in s.split(" "):
        lemmatizer.lemmatize(word)
        if word not in stopwords.words("english"):
            new_s += word + " "
    return new_s[:-1]


def clean(s):
    # remove urls
    s = re.sub(re.compile(r"https?:\/\/(www)?.?([A-Za-z_0-9-]+).*"), "", s)
    # remove emails
    s = re.sub(re.compile(r"\S+@\S+"), "", s)
    # remove punctuation
    s = re.sub(re.compile(r"[^a-z\s]"), "", s)
    # Make everything lowercase
    s = s.lower()
    # remove all personality types
    for type_word in mbti:
        s = s.replace(type_word.lower(), "")
    return s


def prep_counts(s):
    clean_s = clean(s)
    d = {
        "clean_posts": lemmitize(clean_s),
        "link_count": s.count("http"),
        "youtube": s.count("youtube") + s.count("youtu.be"),
        "img_count": len(re.findall(r"(\.jpg)|(\.jpeg)|(\.gif)|(\.png)", s)),
        "upper": len([x for x in s.split() if x.isupper()]),
        "char_count": len(s),
        "word_count": clean_s.count(" ") + 1,
        "qm": s.count("?"),
        "em": s.count("!"),
        "colons": colons(s),
        "emojis": emojis(s),
        "unique_words": unique_words(clean_s),
        "ellipses": len(re.findall(r"\.\.\.\ ", s)),
    }
    return clean_s, d


def prep_sentiment(s):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(s)
    d = {
        "compound_sentiment": score["compound"],
        "pos_sentiment": score["pos"],
        "neg_sentiment": score["neg"],
        "neu_sentiment": score["neu"],
    }
    return d


def tag_pos(s):
    tagged_words = nltk.pos_tag(word_tokenize(s))
    d = dict.fromkeys(tags_dict, 0)
    for tup in tagged_words:
        tag = tup[1]
        for key, val in tags_dict.items():
            if tag in val:
                tag = key
        d[tag] += 1
    return d


def prep_data(s):
    clean_s, d = prep_counts(s)
    d.update(prep_sentiment(lemmitize(clean_s)))
    d.update(tag_pos(clean_s))
    return pd.DataFrame([d])[features]


def combine_classes(y_pred1, y_pred2, y_pred3, y_pred4):
    
    combined = []
    for i in range(len(y_pred1)):
        combined.append(
            str(y_pred1[i]) + str(y_pred2[i]) + str(y_pred3[i]) + str(y_pred4[i])
        )
    
    result = trace_back(combined)
    return result
    

def trace_back(combined):
        
    type_list = [
    {"0": "I", "1": "E"},
    {"0": "N", "1": "S"},
    {"0": "F", "1": "T"},
    {"0": "P", "1": "J"},
    ]

    result = []
    for num in combined:
        s = ""
        for i in range(len(num)):
            s += type_list[i][num[i]]
        result.append(s)
        
    return result


def predict(s):
    return len(s.split(" "))


def predict_e(s):

    X = prep_data(s)

    # loading the 4 models
    with tempfile.TemporaryFile() as fp:
        s3_client.download_fileobj(Fileobj=fp, Bucket=bucket_name, Key='clf_is_Extrovert.joblib')
        fp.seek(0)
        EorI_model = load(fp)
    with tempfile.TemporaryFile() as fp:
        s3_client.download_fileobj(Fileobj=fp, Bucket=bucket_name, Key='clf_is_Sensing.joblib')
        fp.seek(0)
        SorN_model = load(fp)
    with tempfile.TemporaryFile() as fp:
        s3_client.download_fileobj(Fileobj=fp, Bucket=bucket_name, Key='clf_is_Thinking.joblib')
        fp.seek(0)
        TorF_model = load(fp)
    with tempfile.TemporaryFile() as fp:
        s3_client.download_fileobj(Fileobj=fp, Bucket=bucket_name, Key='clf_is_Judging.joblib')
        fp.seek(0)
        JorP_model = load(fp)
    
    # STALE
    # EorI_model = load('./mbti_models/clf_is_Extrovert.joblib')
    # SorN_model = load('./mbti_models/clf_is_Sensing.joblib')
    # TorF_model = load('./mbti_models/clf_is_Thinking.joblib')
    # JorP_model = load('./mbti_models/clf_is_Judging.joblib')

    # predicting
    EorI_pred = EorI_model.predict(X)
    # print("preds", EorI_pred)

    SorN_pred = SorN_model.predict(X)
    # print("preds", SorN_pred)

    TorF_pred = TorF_model.predict(X)
    # print("preds", TorF_pred)

    JorP_pred = JorP_model.predict(X)
    # print("preds", JorP_pred)

    # combining the predictions from the 4 models
    result = combine_classes(EorI_pred, SorN_pred, TorF_pred, JorP_pred)

    return result[0]

def handler(event, context):
    # string = "The idea of love is very vast to us. We need love and compassion to exist."
    string = event['mbti_str']
    mbti = predict_e(string)

    user_table = boto3.resource('dynamodb').Table('user')
    item = user_table.get_item(Key={'user_name': event['user_name']})['Item']
    item['mbti'] = mbti
    user_table.put_item(Item=item)

    conf_table = boto3.resource('dynamodb').Table('book-history')
    item = conf_table.get_item(Key={'confirmation_num': event['confirmation_num']})['Item']
    item['mbti'] = mbti
    conf_table.put_item(Item=item)

    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName='mbti-match',
        InvocationType='RequestResponse',
        Payload=json.dumps({
            'mbti': mbti,
            'user_name': event['user_name'],
            'confirmation_num': event['confirmation_num']
        })
    )
    return response['Payload'].read().decode()
