# Number Guessing Game Objectives:
from random import randint
from guess_the_number_art import logo

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_the_difficulty(difficulty):
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def game():
    print(logo)
    print("Welcome to the number guessing game!")
    attempts = set_the_difficulty(input("Chose your difficulty level. Type 'easy' or 'hard': "))

    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    guess = 0

    while guess != number:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, number, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")


game()
