from random import randint
from turtle import Turtle, Screen


def draw_a_square(start_x, start_y, length):
    timmy.penup()
    timmy.goto(start_x, start_y)
    timmy.pendown()
    timmy.pencolor('green')
    for _ in range(4):
        timmy.right(90)
        timmy.forward(length)


def draw_a_dashed_line(number_of_segments):
    for _ in range(number_of_segments):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def draw_shapes(number_of_shapes):
    for x in range(3, number_of_shapes + 1):
        color = get_random_color()
        timmy.pencolor(color)
        timmy.color(color)
        for side in range(x):
            timmy.forward(100)
            timmy.right(360 / x)


def random_walk(number_of_steps):
    degrees = [0, 90, 180, 270]
    timmy.pensize(10)
    timmy.speed('fastest')
    for x in range(number_of_steps):
        color = get_random_color()
        timmy.pencolor(color)
        timmy.color(color)
        timmy.setheading(degrees[randint(0, 3)])
        timmy.forward(30)


def get_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def draw_a_spirograph(size_og_gap):
    timmy.speed('fastest')
    for x in range(0, 360, size_og_gap):
        color = get_random_color()
        timmy.color(color)
        timmy.pencolor(color)
        timmy.setheading(x)
        timmy.circle(100)


timmy = Turtle()
timmy.shape('turtle')
timmy.color('blue')
screen = Screen()
screen.colormode(255)
# draw_a_square(50, 50, 100)
# draw_a_dashed_line(15)
# draw_shapes(10)
# random_walk(300)
# draw_a_spirograph(15)

screen.exitonclick()
