import random
import turtle as t
color_list = [ (25, 106, 167), (231, 155, 63), (233, 214, 89), (192, 40, 83), (221, 136, 174), (142, 103, 53), (109, 188, 213), (207, 169, 27), (163, 21, 65), (217, 74, 96), (21, 54, 131), (116, 192, 147), (8, 182, 156), (141, 209, 227), (104, 107, 196), (239, 87, 47), (12, 151, 85), (19, 165, 209), (231, 165, 184), (85, 41, 26), (99, 50, 36), (22, 42, 78), (27, 84, 90), (237, 210, 6), (108, 7, 46), (159, 211, 193), (16, 91, 88), (230, 173, 164), (175, 185, 226), (13, 76, 76)]
timmy= t.Turtle()
timmy.shape("turtle")
t.colormode(255)
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
dots = 100

for dots in range(1, dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen= t.Screen()
screen.exitonclick()
