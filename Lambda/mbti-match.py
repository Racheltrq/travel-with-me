import boto3
import pandas as pd
import json
import datetime
from boto3.dynamodb.types import TypeDeserializer

deserializer = TypeDeserializer()
s3 = boto3.client('s3')
ddb = boto3.client('dynamodb')
table_name = 'book-history'


def clean_data(table_name):
    results = []
    last_evaluated_key = None
    while True:
        if last_evaluated_key:
            response = ddb.scan(
                TableName=table_name,
                ExclusiveStartKey=last_evaluated_key
            )
        else: 
            response = ddb.scan(TableName=table_name)
        last_evaluated_key = response.get('LastEvaluatedKey')
        results.extend(response['Items'])
        if not last_evaluated_key:
            break
    for i in range(len(results)):
        results[i] = {k: deserializer.deserialize(v) for k, v in results[i].items()}
    return results


def lambda_handler(event, context):
    mbti, confirmation_num = event['mbti'], event['confirmation_num']
    conf_table = boto3.resource('dynamodb').Table('book-history')
    item = conf_table.get_item(Key={'confirmation_num': confirmation_num})['Item']
    checkin, checkout, city = item['checkin'], item['checkout'], item['hotel_city']
    
    match_df = pd.read_csv(s3.get_object(Bucket='travelwithme-mbti-models', Key='MBTIMatching.csv')['Body'])
    match_mbti = list(set(match_df.iloc[match_df[(match_df['Type']==mbti)].index.tolist()[0]]['Match'].split()))
    
    history, match_users = clean_data(table_name), []
    for each in history:
        if checkout < each['checkin'] or checkin > each['checkout']: break
        else:
            if each['mbti'] in match_mbti and each['hotel_city'] == city:
                match_users.append(each)
    return {
        'statusCode': 200,
        'match': match_users
    }
  
