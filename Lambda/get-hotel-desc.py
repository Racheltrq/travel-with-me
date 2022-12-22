import requests
import json
import boto3
from boto3.dynamodb.types import TypeDeserializer

deserializer = TypeDeserializer()
ddb = boto3.client('dynamodb')
table_name = 'hotel'


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
    hotel_name = event['queryStringParameters']['hotel_name']
    data = clean_data(table_name)
    hotel_desc = []
    for each_hotel in data:
        hotel_desc.append({'hotel_name_trans': each_hotel['hotel_name_trans'], 'description': each_hotel['description']})

    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName='hotel-rec',
        InvocationType='RequestResponse',
        Payload=json.dumps({
            'hotel_name': hotel_name,
            'hotel_list': hotel_desc
        })
    )
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': response['Payload'].read().decode(),
        "isBase64Encoded": False
    }
