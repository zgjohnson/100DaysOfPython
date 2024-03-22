from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        if random.randint(1,6) == 6:
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.pu()
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
