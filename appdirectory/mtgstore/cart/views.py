from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib import messages
import requests
import json

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

def show_cart(request):
    random_cards = get_random_cards()
    card_input_dict = { "cart": random_cards }
    print(card_input_dict)
    return render(request, 'cart/cart.html', card_input_dict)

# Create your views here.
