from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='a', fun=move_counter_clockwise)
screen.onkeypress(key='d', fun=move_clockwise)
screen.onkeypress(key='c', fun=clear_screen)
screen.exitonclick()
