from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

s = Screen()
s.setup(width = 800, height = 600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

s.listen()
s.onkey(r_paddle.up, "Up")
s.onkey(r_paddle.down, "Down")
s.onkey(l_paddle.up, "u")
s.onkey(l_paddle.down, "d")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    
# Detect collision with wall--
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
# Detect collision with paddle--        
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
 # Detect R paddle misses--        
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
# Detect L paddle misses--     
    if ball.xcor() < -380:
        ball.reset_position()    
        score.r_point()
        
s.exitonclick()