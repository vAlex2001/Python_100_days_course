import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkeypress(key="w", fun = player.move_forward)

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move_cars()
    
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
            
            
screen.exitonclick()
