from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.body = []
        self.create_body()

    def create_body(self):
        for position in STARTING_POSITION:
            segment = Turtle(shape='square')
            segment.pu()
            segment.color('white')
            segment.goto(position)
            self.body.append(segment)

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            x = self.body[segment - 1].xcor()
            y = self.body[segment - 1].ycor()
            self.body[segment].goto(x, y)
        self.body[0].forward(MOVE_DISTANCE)
