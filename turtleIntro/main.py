from turtle import Turtle, Screen


def make_square():
    for i in range(0, 4):
        timmy.forward(100)
        timmy.right(90)

def dashed_line():
    for i in range(10):
        timmy.forward(15)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()

timmy = Turtle()
timmy.shape("turtle")
timmy.color("Blue")
make_square()
dashed_line()
screen = Screen()
screen.exitonclick()
