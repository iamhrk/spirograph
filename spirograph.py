from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
circle_obj = Turtle()
circle_obj.speed("fastest")


def color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(72):
    circle_obj.color(color_gen())
    circle_obj.circle(100)
    circle_obj.left(5)

screen.exitonclick()
