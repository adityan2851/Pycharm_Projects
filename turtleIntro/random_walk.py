import turtle as tim
import random

t = tim.Turtle()
tim.colormode(255)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


t.speed("fastest")
direction = [0, 90, 180, 270]
t.pensize(15)
for _ in range(0, 200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(direction))

screen = tim.Screen()
tim.exitonclick()
