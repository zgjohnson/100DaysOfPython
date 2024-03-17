from turtle import Turtle, Screen
import random


def race_setup():
    screen.setup(width=500, height=400)
    colors = ['red', 'orange', 'yellow', 'blue', 'purple']

    y_position = -100
    for color in colors:
        turtle_setup(color, y_position)
        y_position += 45


def turtle_setup(turtle_color, y_pos):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(turtle_color)
    new_turtle.penup()
    new_turtle.goto(-230, y_pos)
    all_turtles.append(new_turtle)


def race():
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            turtle.forward(random.randint(0,10))


screen = Screen()
all_turtles = []
race_setup()
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

if user_bet:
    race()

screen.exitonclick()

