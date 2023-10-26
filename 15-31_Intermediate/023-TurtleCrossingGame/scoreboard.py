from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.pu()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align='left', font=FONT)
        self.road_lines()

    def road_lines(self):
        self.hideturtle()
        self.color("black")
        self.pensize(3)
        self.pu()
        self.goto(310, 250)
        self.seth(180)
        self.pd()
        self.forward(620)
        self.pu()
        self.goto(310, -250)
        self.seth(180)
        self.pd()
        self.forward(620)

    def level_up(self):
        self.level += 1
        self.pu()
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align='left', font=FONT)
        self.road_lines()

    def game_over(self):
        self.color('black')
        self.hideturtle()
        self.pu()
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)
