from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.left(90)
        self.pu()
        self.reset_player_position()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_player_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > 280
