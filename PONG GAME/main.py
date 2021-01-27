from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("white")
screen.title("PONG")
screen.tracer(0)

# line = Turtle(shape="square")
# line.goto(0,0)
# line.shapesize(stretch_len=0.7,stretch_wid=600)
r_ping = Paddle((370,0))
l_ping = Paddle((-370,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_ping.go_up,"w")
screen.onkey(r_ping.go_down,"s")
screen.onkey(l_ping.go_up,"8")
screen.onkey(l_ping.go_down,"2")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        #When the ball collides the y-axis walls and it bounces back
        ball.bounce_y()

    if ball.distance(r_ping) < 50 and ball.xcor() > 340 or ball.distance(l_ping) < 50 and ball.xcor() < -340:
        #When the ball collides the paddles and it bounces back
        ball.bounce_x()

    if ball.xcor() > 400:
        #Scoring the points from the right paddle
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        #Scoring the points from the left paddle
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()