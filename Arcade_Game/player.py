STARTING_POSITION = (0, -280)    
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("indianred")
        self.go_to_start()
        self.setheading(90)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)    
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)    
        
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False    
