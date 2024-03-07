# ############## Blackjack Project #####################
import random

from blackjack_art import logo


# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.
# ############## Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# #################### Hints #####################
# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run


def get_random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, len(cards) - 1)]


def draw_cards(person, number_of_cards):
    for _ in range(number_of_cards):
        card = get_random_card()
        person['cards'].append(card)
    calculate_score(person)


def calculate_score(person):
    if 11 in person['cards'] and sum(person['cards']) > 21:
        change_ace_value(person)
    person['total'] = sum(person['cards'])


def print_cards(player_info, house_info, final):
    if final:
        print(f"\tYour final hand: {player_info['cards']}, final score: {player_info['total']}")
        print(f"\tComputer's final hand: {house_info['cards']}, final score: {house_info['total']}")
    else:
        print(f"\tYour Cards: {player_info['cards']}, current score: {player_info['total']}")
        print(f"\tComputer's first card: {house_info['cards'][0]}")


def change_ace_value(person):
    person['cards'].remove(11)
    person['cards'].append(1)
    person['total'] -= 10


def decide_game(player, house, house_auto_win):
    if house_auto_win:
        print("You lose.")
    elif player['total'] > 21:
        print("You busted. You lose.")
    elif house['total'] > 21:
        print("House busted. You win.")
    elif player['total'] > house['total']:
        print("You win.")
    elif player['total'] == house['total']:
        print("It's a draw.")
    else:
        print("You lose.")


keep_playing = True

while keep_playing:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != 'y':
        keep_playing = False
        continue

    print(logo)

    player = {
        'cards': [],
        'total': 0
    }

    house = {
        'cards': [],
        'total': 0
    }

    draw_cards(player, number_of_cards=2)
    draw_cards(house, number_of_cards=2)

    print_cards(player, house, final=False)

    if house['total'] == 21:
        print_cards(player, house, final=True)
        decide_game(player, house, house_auto_win=True)
        continue
    elif player['total'] == 21:
        player_continue = False
    else:
        player_continue = True

    while player_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            draw_cards(player, number_of_cards=1)
            if player['total'] >= 21:
                player_continue = False
            print_cards(player, house, final=False)
        else:
            player_continue = False

    if player['total'] <= 21:
        while house['total'] < 17:
            draw_cards(house, number_of_cards=1)

    print_cards(player, house, final=True)

    decide_game(player, house, house_auto_win=False)
