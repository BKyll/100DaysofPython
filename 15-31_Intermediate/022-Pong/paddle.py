from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
MOVEMENT_SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.setpos(position)

    def up(self):
        new_y = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

    def new_server(self, position):
        self.goto(position)