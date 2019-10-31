import requests
import json


inventory = []

while len(inventory) < 10:
    url = 'https://api.scryfall.com/cards/random'
    response = requests.get(url)
    responseJson = response.json()
    card = {
        'name':responseJson['name'],
        'price': responseJson['prices']['usd'],
        'image': responseJson['image_uris']['large'],
        'oracleText': responseJson['oracle_text'],
    }
    inventory.append(card)
