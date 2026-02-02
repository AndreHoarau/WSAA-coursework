# Using an api that simulates a deck of cards shuffle and deal 5 cards
# Author: Andre Hoarau
# Import requests to interact with the API and minidom to parse and interact with the XMLs
import requests
from xml.dom import minidom
# Url for shuffling
url_shuffle = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
# As per the documentation a get should shuffle the deck
shuffle_deck = requests.get(url_shuffle)
print(shuffle_deck)
# This gives a response code of 200 which is good it means that it works and we can parse the xml.
# The response is not an XML this time but a JSON
doc = shuffle_deck.json()
deck_id = doc['deck_id']
print(deck_id)
print(doc)
# So now we have the deck id of our shuffled deck. 
url_deal = 'https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=5'
deck_deal = requests.get(url_deal)
deal = deck_deal.json()
cards = deal['cards']
for card in cards:
    print(f'{card['value']} of {card['suit']}')

