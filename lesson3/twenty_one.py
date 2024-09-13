import random
import json
import os

def clear_screen():
    os.system('clear')

def prompt(message):
    print(f'==> {message}')

def initialize_deck():
    suits = [suit for suit in 'HDSC']
    values = [card for card in '23456789JQKA']
    return [[suit, value] for suit in suits for value in values]        

def deal_player_cards(deck):
    card_one = random.choice(deck)
    deck.remove(card_one)
    card_two = random.choice(deck)
    deck.remove(card_two)

    player_hand = [card_one, card_two]

    return player_hand, deck

def deal_dealer_cards(deck):
    card_one = random.choice(deck)
    deck.remove(card_one)
    card_two = random.choice(deck)
    deck.remove(card_two)

    dealer_hand = [card_one, card_two]

    return dealer_hand, deck

def replay_game():
    prompt(messages['replay'])

    if not is_yes():
        prompt(messages['goodbye'])
        return False

    return True

def is_yes():
    answer = input().lower().strip()

    while answer not in ['y', 'n']:
        prompt(messages['invalid_input'])
        prompt(messages['replay_options'])
        answer = input().lower()

    return bool(answer == 'y')

def play_twenty_one():
    while True:
        deck = initialize_deck()
        player_hand, deck = deal_player_cards(deck)
        dealer_hand, deck = deal_dealer_cards(deck)

        if not replay_game():
            break



with open('ttt_messages.json', 'r') as file:
    messages = json.load(file)

play_twenty_one()