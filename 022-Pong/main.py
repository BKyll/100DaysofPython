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
from paddle import Paddle
from ball import Ball
import time

# Field
field = Screen()
field.setup(800, 600)
field.bgcolor("black")
field.title("PONG")
field.tracer(0)

net = Turtle()
net.hideturtle()
net.color("white")
net.pensize(5)
net.pu()
net.goto(0, 280)
net.seth(270)
for _ in range(19):
    net.pd()
    net.forward(10)
    net.pu()
    net.forward(20)

score = Scoreboard()

# Paddles
r_start = (350, 0)
l_start = (-350, 0)
r_paddle = Paddle(r_start)
l_paddle = Paddle(l_start)

field.listen()
field.onkey(r_paddle.up, 'Up')
field.onkey(r_paddle.down, 'Down')
field.onkey(l_paddle.up, 'w')
field.onkey(l_paddle.down, 's')

# Ball
ball = Ball()


def reset_game():
    ball.new_serve()
    r_paddle.new_server(r_start)
    l_paddle.new_server(l_start)


# Main
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    field.update()
    ball.move_ball()

    # Hitting a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Hitting a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 330 or ball.distance(l_paddle) < 50 and ball.xcor() <= -330:
        ball.bounce_x()

    # Scoring a goal
    if ball.xcor() > 380:
        score.score('l')
        reset_game()

    if ball.xcor() < -380:
        score.score('r')
        reset_game()
