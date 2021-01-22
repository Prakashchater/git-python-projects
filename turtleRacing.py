from turtle import Turtle,Screen
import turtle
import random
screen = Screen()
screen.setup(height=500,width=530)
is_race_on= False
color= ["violet","indigo","blue","green","yellow","orange","red"]
all_turtle = []
y_position = [-70,-40,-10,20,50,80,110]
for i in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[i])
    all_turtle.append(new_turtle)
user_bet = screen.textinput("Make your bet","Enter the turtle color you want to bet on: ")

if user_bet:
    is_race_on = True
while is_race_on:
    for turtles in all_turtle:
        if turtles.xcor()>235:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won the race. The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost the race. The {winning_color} turtle is the winner.")
        distance = random.randint(0,10)
        turtles.forward(distance)
screen.exitonclick()
