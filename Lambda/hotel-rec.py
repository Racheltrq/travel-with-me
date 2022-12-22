# This file lives in an Amazon ECR container.
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import re
import random
import pandas as pd
pd.options.display.max_columns = 30
import nltk
from nltk.corpus import stopwords
nltk.data.path.append("/tmp")
nltk.download('stopwords', download_dir="/tmp")

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')


# get top k of n-gram in all hotel descriptions
def get_top_n_words(corpus, n=1, k=None):
    # n-gram word frequency matrix
    vec = CountVectorizer(ngram_range=(n, n), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    # print('feature names:')
    # print(vec.get_feature_names())
    # print('bag of words:')
    # print(bag_of_words.toarray())
    
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:k]


def clean_text(text):
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    text = ' '.join(word for word in text.split() if word not in stopwords.words("english")) 
    return text


def recommendations(name, cosine_similarities, df, indices):
    recommended_hotels = []
    # given hotel name, find index of it
    idx = indices[indices == name].index[0]
    # calculate cosine similarities, then sort result
    score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending = False)
    top_10_indexes = list(score_series.iloc[1:11].index)  # need to exclude self
    for i in top_10_indexes:
        recommended_hotels.append(list(df.index)[i])
    return recommended_hotels


def handler(event, context):
    df = pd.DataFrame.from_records(event['hotel_list'])
    df['description'] = df['description'].apply(clean_text)
    df.set_index('hotel_name_trans', inplace = True)
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0.01, stop_words='english')
    tfidf_matrix = tf.fit_transform(df['description'])

    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(df.index)
    print(recommendations(event['hotel_name'], cosine_similarities, df, indices))
    return recommendations(event['hotel_name'], cosine_similarities, df, indices)
