import random
import json
import os

def clear_screen():
    os.system('clear')

def prompt(message):
    print(f'==> {message}')

def initialize_deck():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9',
              'Jack', 'Queen', 'King', 'Ace']
    return [[value, suit] for suit in suits for value in values]

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

def display_hands(player, dealer):
    prompt(messages['dealer_hand'].format(dealer = dealer))
    prompt(messages['player_hand'].format(player = player))


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
        print(player_hand)
        print(dealer_hand)
        print(deck)
        display_hands(player_hand, dealer_hand)
        # player_choice()
        # dealer_choice()
        # calculate_score()
        # display_result()
        if not replay_game():
            break



with open('twenty_one_messages.json', 'r') as file:
    messages = json.load(file)

play_twenty_one()