from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def moveup(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)