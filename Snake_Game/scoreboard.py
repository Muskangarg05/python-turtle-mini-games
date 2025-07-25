from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read().strip())
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align = ALLIGNMENT, font = FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()        
        
   