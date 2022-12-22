import json
import boto3
import time
from boto3.dynamodb.conditions import Key

user_table = boto3.resource('dynamodb').Table('user')
conf_table = boto3.resource('dynamodb').Table('book-history')


def lambda_handler(event, context):
    user_name = event['queryStringParameters']['user_name']
    mbti_str = event['queryStringParameters']['mbti_str']
    
    item = user_table.get_item(Key={'user_name': user_name})['Item']
    item['mbti_str'] = mbti_str
    user_table.put_item(Item=item)
    
    confirmation_num = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(time.time()).replace('.', '')[-7:])
    conf_info = {
        'confirmation_num': confirmation_num,
        'user_name': user_name, 'phone': item['phone'], 'user_email': item['user_email'],
        'hotel_name': event['queryStringParameters']['hotel_name'],
        'hotel_city': event['queryStringParameters']['hotel_city'],
        'checkin': event['queryStringParameters']['duration'].split(',')[0],
        'checkout': event['queryStringParameters']['duration'].split(',')[1]
    }
    conf_table.put_item(Item=conf_info)
    
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName='mbti-pred',
        InvocationType='RequestResponse',
        Payload=json.dumps({
            'user_name': user_name, 'mbti_str': mbti_str,
            'confirmation_num': confirmation_num
        }),
    )
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': response['Payload'].read().decode().replace('\"', '"').replace('\\', '')[1:-1],
        "isBase64Encoded": False
    }
