import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

road = Screen()
road.setup(width=600, height=600)
road.tracer(0)
road.title("TURTLER")

turtler = Player()
user_interface = Scoreboard()
car_manager = CarManager()

road.listen()
road.onkey(turtler.up, ' ')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    road.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.cars:
        if car.distance(turtler) < 20:
            user_interface.game_over()
            game_is_on = False

    if turtler.crossed_finish():
        user_interface.level_up()
        turtler.next_level()
        car_manager.increase_speed()

road.exitonclick()
