# Snake Game

# Day 20
# Create a snake body
# Move the snake
# Control the snake

# Day 21
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with self

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("dimgrey")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
