# ############## Blackjack Project #####################
import random

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

from blackjack_art import logo


def get_random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, len(cards) - 1)]


def draw_cards(number_of_cards, person):
    for _ in range(number_of_cards):
        card = get_random_card()
        person['cards'].append(card)
        person['total'] += card


def print_cards(player, house, final):
    if final:
        print(f"\tYour final hand: {player['cards']}, final score: {player['total']}")
        print(f"\tComputer's final hand: {house['cards']}, final score: {house['total']}")
    else:
        print(f"\tYour Cards: {player['cards']}, current score: {player['total']}")
        print(f"\tComputer's first card: {house['cards'][0]}")


def change_ace_value(person):
    person['cards'].remove(11)
    person['cards'].append(1)
    person['total'] -= 10


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

    draw_cards(2, player)
    draw_cards(2, house)

    print_cards(player, house, False)

    if house['total'] == 21:
        player_continue = False
        house_auto_win = True
    else:
        player_continue = True
        house_auto_win = False

    while player_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            draw_cards(1, player)
            if player['total'] > 21:
                if 11 in player['cards']:
                    change_ace_value(player)
                else:
                    player_continue = False
            print_cards(player, house, False)
        else:
            player_continue = False

    if player['total'] <= 21:
        while house['total'] < 17:
            draw_cards(1, house)
            if house['total'] > 21 and 11 in house['cards']:
                change_ace_value(house)

    print_cards(player, house, True)

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
