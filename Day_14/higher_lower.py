
from os import system
from art import logo, vs
from random import randint
from game_data import data


def get_random_person():
    return data[randint(0, len(data) - 1)]


def format_person_info(person):
    return f'{person['name']}, a {person['description']}, from {person['country']}'


def print_round_info(person_a, person_b, player_score):
    print(logo)
    if player_score > 0:
        print(f"You're right! Current score: {player_score}.")
    print(f"Compare A: {format_person_info(person_a)}.")
    print(vs)
    print(f"Compare B: {format_person_info(person_b)}.")


def get_answer(follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return 'a'
    else:
        return 'b'


def high_low_game():
    continue_game = True
    person_b = get_random_person()

    score = 0
    while continue_game:

        person_a = person_b
        person_b = get_random_person()
        while person_a == person_b:
            person_b = get_random_person()

        print_round_info(person_a, person_b, score)
        answer = get_answer(person_a['follower_count'], person_b['follower_count'])
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if guess == answer:
            score += 1
        else:
            continue_game = False

        system('cls')

    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


high_low_game()
