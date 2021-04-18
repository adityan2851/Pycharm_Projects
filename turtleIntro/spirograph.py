import turtle as t
import random
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim = t.Turtle()
tim.speed("fastest")
for _ in range (0, 73):
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)

screen = t.Screen()
screen.exitonclick()