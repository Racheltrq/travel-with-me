import json
import requests
import boto3
import numpy as np
import pandas as pd
from dynamo_pandas import put_df, get_df, keys
from bs4 import BeautifulSoup
import csv

rapidapi_access_key = 'c055fae240msh31b68691fe427bbp1dcee8jsnfdd957b92e9e'
rapidapi_host = 'booking-com.p.rapidapi.com'


def getDestId(LOC):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
    params = {"locale": 'en-us', "name": LOC}
    headers = {
        "X-RapidAPI-Key": rapidapi_access_key, "X-RapidAPI-Host": rapidapi_host
    }
    response = requests.request("GET", url, headers=headers, params=params)
    return (response.json()[0]['dest_id'], response.json()[0]['dest_type'])


def searchHotel(dest_info, GUEST_PREF, page_index):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
    params = {
        "checkout_date":GUEST_PREF[6], "units":"metric",
        "dest_id":dest_info[0], "dest_type":dest_info[1], "locale": 'en-us',
        "adults_number":GUEST_PREF[0], "order_by":"popularity",
        "filter_by_currency":"USD", "checkin_date":GUEST_PREF[5],
        "room_number":GUEST_PREF[3], "children_number":GUEST_PREF[1],
        "page_number":str(page_index), "include_adjacency":"true",
        "children_ages":GUEST_PREF[2], "categories_filter_ids":GUEST_PREF[4]
    } if GUEST_PREF[1] != 0 else {
        "checkout_date":GUEST_PREF[6], "units":"metric",
        "dest_id":dest_info[0], "dest_type":dest_info[1], "locale": 'en-us',
        "adults_number":GUEST_PREF[0], "order_by":"popularity",
        "filter_by_currency":"USD", "checkin_date":GUEST_PREF[5],
        "room_number":GUEST_PREF[3],
        "page_number":str(page_index), "include_adjacency":"true",
        "categories_filter_ids":GUEST_PREF[4]
    }
    headers = {
        "X-RapidAPI-Key": rapidapi_access_key, "X-RapidAPI-Host": rapidapi_host
    }
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.json())
    return response.json()


# Function "search" workflow:
# 1. Give location name, abbreviation or any other forms (`LOC`).
# 2. Feed `LOC` to getDestId. It returns an unique destination id info (`dest_info`).
# 3. Feed `dest_info`, `GUEST_PREF` to searchHotel. It returns search results.
def search(round, LOC, GUEST_PREF):
    dest_info = getDestId(LOC)
    result = []
    for i in range(round):
        hotels_res = searchHotel(dest_info, GUEST_PREF, i)
        for j in range(len(hotels_res['result'])):
            keys = np.array(list(hotels_res['result'][j].keys()))
            values = np.array(list(hotels_res['result'][j].values()))
            arrIndex = np.array(keys).argsort()
            keys, values = keys[arrIndex].tolist(), values[arrIndex].tolist()
            result.append(values)
    csvpath = '/tmp/search_result.csv'
    with open(csvpath, 'w') as f:
        csv.writer(f).writerow(keys)
        for each_hotel in result:
            csv.writer(f).writerow(each_hotel)
    return result


def lambda_handler(event, context):
    try:
        # search location
        LOC = str(event['queryStringParameters']['location'])
        # guest preference, including adults number (index 0), children number (index 1),
        # children ages (index 2) room number (index 3), free cancellation (index 4)
        # checkin date (index 5), checkout date (index 6)
        GUEST_PREF = (
            int(event['queryStringParameters']['adults_number']), int(event['queryStringParameters']['children_number']),
            str(event['queryStringParameters']['children_age']), int(event['queryStringParameters']['room_number']),
            'free_cancellation::1' if int(event['queryStringParameters']['free_cancellation']) else 'free_cancellation::0',
            str(event['queryStringParameters']['checkin_date']), str(event['queryStringParameters']['checkout_date'])
        )
    except:
        LOC, GUEST_PREF = 'Boston', (2, 1, '5', 1, 'free_cancellation::1', '2023-03-15', '2023-03-22')
    
    result = search(2, LOC, GUEST_PREF)
    
    s3 = boto3.resource("s3")
    s3.meta.client.upload_file('/tmp/search_result.csv', 'travelwithme-mbti-models', 'search_result.csv')
    
    cols = ['accommodation_type_name', 'address_trans', 'cant_book', 'cc1', 'checkin',
       'checkout', 'children_not_allowed', 'city_name_en', 'class', 'composite_price_breakdown',
       'country_trans', 'currency_code', 'district', 'hotel_id', 'hotel_name_trans',
       'is_free_cancellable', 'is_smart_deal', 'latitude', 'longitude', 'price_breakdown',
       'review_nr', 'review_score_word', 'soldout', 'timezone', 'unit_configuration_label',
       'url', 'zip', 'max_photo_url']
    df = pd.read_csv('/tmp/search_result.csv', usecols=cols, index_col=False).dropna().reset_index(drop=True)
    
    for i in range(len(df)):
        if df['hotel_name_trans'][i].startswith('property_card') or df['hotel_name_trans'][i] == '0':
            response = requests.request("GET", df.loc[i, 'url'])
            id_start = response.text.find('b_hotel_id: ')
            name_start = response.text.find('b_hotel_name: ')
            name_end = response.text.find('b_hotel_image_url_square60: ')
            hotel_id = BeautifulSoup(response.text[id_start+13:name_start-3]).get_text(strip=True)
            hotel_name = BeautifulSoup(response.text[name_start+15:name_end-3]).get_text(strip=True)
            df.loc[i, 'hotel_id'], df.loc[i, 'hotel_name_trans'] = hotel_id, hotel_name
    
    rtn_res = []
    for _, each in df.iterrows():
        price_breakdown = json.loads(each['price_breakdown'].replace("'", "\""))
        if isinstance(price_breakdown, dict):
            rtn_res.append({'name': each['hotel_name_trans'], 'address': each['address_trans'],
                'score': each['review_score_word'], 'pic_url': each['max_photo_url'],
                'price': price_breakdown['all_inclusive_price']
            })
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(rtn_res),
        "isBase64Encoded": False
    }
