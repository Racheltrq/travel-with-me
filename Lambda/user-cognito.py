import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user')


def lambda_handler(event, context):
    user_name = event['userName']
    
    user_email = event['request']['userAttributes']['email']
    full_name = event['request']['userAttributes']['name']
    gender = event['request']['userAttributes']['gender']
    phone_number = event['request']['userAttributes']['phone_number']
    response = table.put_item(Item={
        'user_name':user_name, 'user_email':user_email, 'name': full_name,
        'gender': gender, 'phone': phone_number
    })
    return {
        'statusCode': '200',
        'body': json.dumps('User successfully pushed to DDB!')
    }
  
