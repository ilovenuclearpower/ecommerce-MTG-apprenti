from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib import messages
import asyncio
import requests
import json

async def get_random_cards():
    inventory = []

    while len(inventory) < 10:
        url = 'https://api.scryfall.com/cards/random'
        value = await requests.get(url)
        responseJson = value.json()
        card = {
            'name':responseJson['name'],
            'price': responseJson['prices']['usd'],
            'image': responseJson['image_uris']['large'],
            'oracleText': responseJson['oracle_text'],
        }
        inventory.append(card)
    return inventory

def show_cart(request):
    loop = asyncio.new_event_loop()
    cart = loop.run_until_complete(get_random_cards())
    return render(request, 'cart/cart.html', cart)

# Create your views here.
