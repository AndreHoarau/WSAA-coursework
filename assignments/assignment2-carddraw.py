# Using an api that simulates a deck of cards shuffle and deal 5 cards
# Author: Andre Hoarau
# Import requests to interact with the API import counter to count the doubles and triples 
#Counter documentation = https://docs.python.org/3/library/collections.html#collections.Counter
import requests
from collections import Counter
# Url for shuffling
url_shuffle = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
# As per the documentation a get should shuffle the deck https://www.deckofcardsapi.com/
shuffle_deck = requests.get(url_shuffle)
print(shuffle_deck)
# This gives a response code of 200 which is good. The response is a JSON.
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
        values_assigned.append(int(v))
    else:
        values_assigned.append(face_card_values[v])
print(values_assigned)

# Check for pairs / triples
counts = Counter(values_assigned)
pairs = [v for v, cnt in counts.items() if cnt == 2]
triples = [v for v, cnt in counts.items() if cnt == 3]

if triples:
    print("You have a triple! Congratulations!")
elif pairs:
    print("You have a pair! Congratulations!")

# Check for straight
sorted_values = sorted(values_assigned)
if sorted_values == list(range(min(sorted_values), min(sorted_values) + 5)):
    print("You have a straight! Congratulations!")

# Check for flush
if len(set(suits)) == 1:
    print("You have a flush! All cards of the same suit! Congratulations!")