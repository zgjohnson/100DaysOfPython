from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.pu()
        self.y_move = 10
        self.x_move = 10
        self.velocity = 1

    def move(self):
        new_x = self.xcor() + self.x_move * self.velocity
        new_y = self.ycor() + self.y_move * self.velocity
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.velocity += 0.5

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.velocity = 1
        self.bounce_x()
