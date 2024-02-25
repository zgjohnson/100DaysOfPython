print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input("left or right?\n").lower()

if first_choice != "left":
    print("You fell into a hole. Game Over.")
else:
    second_choice = input("You come across a big lake, do you swim or wait?\n").lower()
    if second_choice != "wait":
        print("You were eaten by a shart. Game Over.")
    else:
        third_choice = input(
            """Your wait is succesfull. A boat comes along and takes you to an islan. 
                You come across three doors of different colors. Which do you choose? Red, Yellow, or Blue.\n"""
        ).lower()

        if third_choice == "yellow":
            print("You found the treasure! You Win!")
        elif third_choice == "red":
            print(
                "You walk into a room full of fire. You are burnt to a crisp. Game Over."
            )
        elif third_choice == "blue":
            print("You fall into a void of darkness and despair. Game Over.")
        else:
            print("Wrong choice. Game Over.")
