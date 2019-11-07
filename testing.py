
from django.shortcuts import render
import urllib.parse
import requests
import pdb
import asyncio

def get_cards_from_scryfall_query(query_string):
    inventory = []
    print(query_string)
    url = 'https://api.scryfall.com/cards/search?q=' + urllib.parse.quote(query_string)
    print(url)
    api_returned_cards = requests.get(url)
    if api_returned_cards.status_code == 404:
        return None
    returned_cards_json = api_returned_cards.json()
    for i in range(len(returned_cards_json["data"])):
        card = {
            'name':returned_cards_json["data"][i]['name'],
            'price': returned_cards_json["data"][i]['prices']['usd'],
            'image': returned_cards_json["data"][i]['image_uris']['small'],
            'oracleText': returned_cards_json["data"][i]['oracle_text'],
        }
        inventory.append(card)
    return inventory
def get_random_cards():
    inventory = []

    while len(inventory) < 10:
        url = 'https://api.scryfall.com/cards/random'
        value = requests.get(url)
        responseJson = value.json()
        card = {
            'name':responseJson['name'],
            'price': responseJson['prices']['usd'],
            'image': responseJson['image_uris']['small'],
            'oracleText': responseJson['oracle_text'],
        }
        inventory.append(card)
    return inventory


value = get_cards_from_scryfall_query("awe;krgfjuhgasdlfkg;jhasg")
print(value)
=======
#!/usr/bin/env python
import boto3
import psycopg2

session = boto3.session.Session()
client = session.client('rds', region_name='us-east-2')
token = client.generate_db_auth_token('database-django-apprenti-testing-fifthtry.cebxmljii3h7.us-east-2.rds.amazonaws.com',5432,'djangoapp')
ssl = {'ca': 'rds-combined-ca-bundle.pem'} 
print(token)
conexao = psycopg2.connect(host='database-django-apprenti-testing-fifthtry.cebxmljii3h7.us-east-2.rds.amazonaws.com',port=5432,user='djangoapp',password=token, database="django")

