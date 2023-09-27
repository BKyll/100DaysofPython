from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        x = random.randint(-28, 28) * 10
        y = random.randint(-28, 28) * 10
        self.goto(x, y)
