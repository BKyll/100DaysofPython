from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.shape("turtle")
        self.seth(90)
        self.setpos(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def crossed_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def next_level(self):
        self.setpos(STARTING_POSITION)

