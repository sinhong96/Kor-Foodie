import ast
import csv
import pandas as pd
import requests
import urllib
import json
from urllib.parse import quote_plus
from urllib.parse import urlencode
import pprint
import json

def retrieve_info(food_name):

    apikey = f"0P3Bpj4s%2BLxNZosirHCvbNmNAGOt1iL8I3hRd4ww70oqJ%2FDeDD%2FVY3qYoFZHGnWffVf%2B04oV7PQH%2B%2FJu7ed%2BrA%3D%3D"
    
    url = 'http://apis.data.go.kr/1471000/FoodNtrIrdntInfoService1/getFoodNtrItdntList1'
    # params ={'serviceKey' : apikey, 'desc_kor' : '바나나칩', 'pageNo' : '1', 'numOfRows' : '3', 'bgn_year' : '2017', 'animal_plant' : '(유)돌코리아', 'type' : 'xml' }


    # class_names = open("./class/class_namesV3.txt", "r", encoding= 'UTF-8').read().split('\n')

    desc_kor = food_name # '초코쿠키' # '가츠동'
    queryParams = f'?{quote_plus("ServiceKey")}={apikey}&' + urlencode({ 
        quote_plus('desc_kor') : desc_kor , 
        quote_plus('type') : 'json', 
        })
    response = requests.get(url + queryParams) # requests.get(url, params=queryParams)
    response_data = response.json()

    if response_data['body']['totalCount'] == 0:
        print(desc_kor, " no available from API")

        pretty_dict_str = response_data

    elif response_data['body']['totalCount'] != 0:
        list_of_dict = response_data['body']['items'] 
        my_json = json.dumps(list_of_dict)
        # print(my_json)

        listt = ast.literal_eval(my_json)
        # print(listt)

        # just get the first result
        retrieved_info_1 = listt[0]

        return retrieved_info_1