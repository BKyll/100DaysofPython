# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score
from turtle import Screen, Turtle
from score import Scoreboard
import time

field = Screen()
field.setup(1000, 600)
field.bgcolor("black")
field.title("PONG")
field.tracer(0)

net = Turtle()
net.color("white")
net.pensize(5)
net.shape("square")
net.pu()
net.goto(0, 280)
net.seth(270)
for _ in range(19):
    net.pd()
    net.forward(10)
    net.pu()
    net.forward(20)

score = Scoreboard()

game_is_on = True
while game_is_on:
    field.update()
    time.sleep(0.1)

field.exitonclick()
