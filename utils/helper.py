import csv
import os
import requests
import json

base_folder = os.path.abspath('.')
input_file = os.path.join(base_folder +'/datas', 'products.csv')

def readdatas():
    datas = []
    with open(input_file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter='|')
        next(data)  
        for row in data:
            datas.append(row)
    return datas

def getresponsetext(api_url):
    response = requests.get(api_url)
    response_data = json.loads(response.text)
    return response_data

def getresponse(api_url):
    response = requests.get(api_url)
    return response