from turtle import Turtle
from ball import Ball

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.hideturtle()
        self.pu()
        self.write_scores()

    def write_scores(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def score(self, side):
        if side == 'r':
            self.r_score += 1
        elif side == 'l':
            self.l_score += 1
        self.clear()
        self.write_scores()
