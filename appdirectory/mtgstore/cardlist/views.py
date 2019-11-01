from django.shortcuts import render
import urllib.parse
import requests
# Create your views here.

## Takes in a query string and sends it to the scryfall api.
## I would prefer to do this async, but I don't want to import django packages.
## We are only capturing the values we want from the database.
## Potential optimizations: Add a caching solution to cache these returns in case 
## Multiple users are making the same queries.
def get_cards_from_scryfall_query(query_string):
    inventory = []
    print(query_string)
    url = 'https://api.scryfall.com/cards/search?q=' + urllib.parse.quote(query_string)
    api_returned_cards = requests.get(url)
    print(api_returned_cards)
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


## We have to convert the list that the get_cards_from_scryfall_query
## to a dict, for passing in to the render method as a context object.
def search_card_list(request):
    ##Not sure how to validate/guarantee inputs here, for now we just "know" that we need to send it as a value for the "q" variable to work.
    ##This is not good in case more than one page/developer wants to render a list of cards from more than one place.
    print(request)
    search_string = request.GET.get("q", "")
    if search_string == "":
        return render(request, "cardlist/totallylost.html")
    scryfall_card_list = get_cards_from_scryfall_query(search_string)
    card_list_for_display = {}
    for i in range(len(scryfall_card_list)):
        card_list_for_display["card" + str(i)] = scryfall_card_list[i]
    return render(request, "cardlist/cardlist.html", card_list_for_display)

def show_blank(request):
    return render(request, "cardlist/totallylost.html")

