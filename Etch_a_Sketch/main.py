from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def backwards():
    timmy.backward(10)


def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def clear():
    timmy.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
