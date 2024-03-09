import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def play_a_game():
    game_images = [rock, paper, scissors]
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        return "Invalid Choice."

    computer_choice = random.randint(0, 2)

    decision = [
        ["Its a draw.", "You lose.", "You win."],
        ["You win.", "Its a draw.", "You lose."],
        ["You lose.", "You win.", "Its a draw."]
    ]

    print(game_images[user_choice])

    print(f"Computer Chose: {game_images[computer_choice]}")

    return decision[user_choice][computer_choice]


keep_playing = True
while keep_playing:
    outcome = play_a_game()
    print(outcome)
    if input("Want to play again? (y/n): ") != 'y':
        keep_playing = False

print("Game Over!")
