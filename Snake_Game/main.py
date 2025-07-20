from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from  scoreboard import Scoreboard

s = Screen()
s.setup(width = 600, height = 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

    
game_is_on = True
while game_is_on:    
    s.update()
    time.sleep(0.1)
    snake.move_snake() 

# Detect collision with food--    
    if snake.head.distance(food) < 15:
        food.refresh() 
        snake.extend()
        score.increase_score()

 # Detect collision with wall--        
    if (snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300):   
        score.reset()
        snake.reset()

# Detect collision with tail--        
    for segment in snake.segments[1:]:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset() 
            snake.reset()  
          
s.exitonclick()
 