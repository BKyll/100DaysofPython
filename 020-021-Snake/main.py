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
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("dimgrey")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

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

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()

    # Detect collision with wall.
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        game_is_on = False
        score.gameover()


screen.exitonclick()
