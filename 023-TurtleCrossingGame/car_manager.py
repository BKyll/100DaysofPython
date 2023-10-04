from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        r = random.randint(1, 6)
        if r == 1:
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.pu()
            y_pos = random.randint(-235, 235)
            new_car.setpos(315, y_pos)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
