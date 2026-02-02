# Using an api that simulates a deck of cards shuffle and deal 5 cards
# Author: Andre Hoarau
# Import requests to interact with the API and minidom to parse and interact with the XMLs
import requests
from collections import counter
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
# The above url deals the cards so we insert our shuffled deck.
deck_deal = requests.get(url_deal)
deal = deck_deal.json()
cards = deal['cards']
# Setting up lists for the values and suits to explore looking at card combinations.
values = []
suits = []
# Then looking at each card in turn we can print their value and suit.
for card in cards:
    print(f'{card['value']} of {card['suit']}')
    values.append(card['value'])
    suits.append(card['suit'])
# As the face cards can also be part of straight we need to assign a numeric value to them for simplicity Ace will just be the highest card.
face_card_values = {
    "ACE": 14,
    "KING": 13,
    "QUEEN": 12,
    "JACK": 11
}
values_assigned =[]
for v in values:
    if v.isdigit():
        values_assigned.append(v)
    else:
        values_assigned.append(face_card_values[v])
print(values_assigned)