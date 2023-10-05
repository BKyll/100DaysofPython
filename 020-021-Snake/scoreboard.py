from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("G:\\My Drive\\100DaysofPython\\020-021-Snake\\data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.hideturtle()
        self.pu()
        self.goto(0, 270)
        self.update_scoreboard()

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("G:\\My Drive\\100DaysofPython\\020-021-Snake\\data.txt", mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
