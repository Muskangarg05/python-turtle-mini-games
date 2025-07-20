import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(tim.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()  
     
 # Detect collision with car--    
    for running_car in car.all_cars:
        if running_car.distance(tim) < 20:
            game_is_on = False  
            score.game_over()
 
# Detect successful crossing--               
    if tim.is_at_finish_line():
        tim.go_to_start()
        car.level_up()
        score.incerease_level()
        
screen.exitonclick()