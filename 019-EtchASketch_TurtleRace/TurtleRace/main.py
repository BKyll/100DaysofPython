from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Who will win?", prompt=f"Which turtle will win the race? Enter a color:\n{colors}")
all_turtles = []

for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.pu()
    t.goto(-230, 90 - (turtle_index * 30))
    all_turtles.append(t)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = str(turtle.pencolor())

if user_bet == winning_turtle:
    print(f"You win! {winning_turtle.capitalize()} was the fastest!")
else:
    print(f"Sorry, you lose. {winning_turtle.capitalize()} was the fastest.")

screen.exitonclick()
