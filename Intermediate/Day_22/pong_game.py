import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with a paddle
    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 320)
            or (ball.distance(left_paddle) < 50 and ball.xcor() < - 320)):
        ball.bounce_x()

    # Detect if a paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
