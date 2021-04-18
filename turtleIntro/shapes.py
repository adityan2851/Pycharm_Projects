from turtle import Turtle, Screen
import random

timmy = Turtle()

colors = ["Cornflowerblue", "Red", "Blue", "Green", "wheat", "slategray", "Black"]


def start():
    for i in range(3, 11):
        current_angle = 360 / i
        timmy.color(random.choice(colors))
        while i:
            timmy.forward(100)
            timmy.right(current_angle)
            i -= 1


start()
screen = Screen()
screen.exitonclick()
