# Step 5
import os
import random
from hangman_word import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

used_letters = []

while not end_of_game:

    guess = input("Guess a letter: ").lower()
    os.system('cls')

    if guess in used_letters:
        print("You have already guessed the letter: " + guess)
    else:
        used_letters.append(guess)
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
