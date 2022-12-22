import json
import requests
from dynamo_pandas import put_df, get_df, keys
import pandas as pd
from bs4 import BeautifulSoup
import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket='travelwithme-mbti-models', Key='search_result.csv')['Body']
    cols = ['accommodation_type_name', 'address_trans', 'cant_book', 'cc1', 'checkin',
       'checkout', 'children_not_allowed', 'city_name_en', 'class', 'composite_price_breakdown',
       'country_trans', 'currency_code', 'district', 'hotel_id', 'hotel_name_trans',
       'is_free_cancellable', 'is_smart_deal', 'latitude', 'longitude', 'price_breakdown',
       'review_nr', 'review_score_word', 'soldout', 'timezone', 'unit_configuration_label',
       'url', 'zip', 'max_photo_url']
    df = pd.read_csv(obj, usecols=cols, index_col=False).dropna().reset_index(drop=True)
    
    # add description to valid results
    for i in range(len(df)):
        response = requests.request("GET", df.loc[i, 'url'])
        des_start = response.text.find('<div id="property_description_content">')
        des_len = response.text[des_start:].find('</div>') + 6
        des = BeautifulSoup(response.text[des_start:des_start + des_len]).get_text(strip=True)
        df.loc[i, 'description'] = des
        if not str(df['hotel_id'][i]).isdigit() or str(df['hotel_id'][i]) == '0':
            id_start = response.text.find('b_hotel_id: ')
            name_start = response.text.find('b_hotel_name: ')
            name_end = response.text.find('b_hotel_image_url_square60: ')
            hotel_id = BeautifulSoup(response.text[id_start+13:name_start-3]).get_text(strip=True)
            hotel_name = BeautifulSoup(response.text[name_start+15:name_end-3]).get_text(strip=True)
            df.loc[i, 'hotel_id'], df.loc[i, 'hotel_name_trans'] = hotel_id, hotel_name
    df['hotel_id'] = pd.to_numeric(df['hotel_id'])
    print('PUSHING HOTEL DATA TO DDB...')
    put_df(df, table="hotel")
    print('HOTEL DATA PUSHED!')
    return {
        'statusCode': 200,
        'body': json.dumps('Search result pushed to DynamoDB!')
    }
