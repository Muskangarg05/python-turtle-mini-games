COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random as r

class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_cars(self): 
        self.random_chance = r.randint(1, 6)
        
        if self.random_chance == 1:      
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(r.choice(COLORS))
            new_car.shapesize(stretch_len = 2, stretch_wid = 1)
            random_y = r.randint(-280, 280)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
            
    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)   
        
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    