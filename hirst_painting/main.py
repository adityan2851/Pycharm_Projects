# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
import random
import turtle as t


tim = t.Turtle()
tim.hideturtle()
screen = t.Screen()
t.colormode(255)

color_list = [(227, 227, 225), (249, 212, 93), (150, 69, 97), (53, 99, 155), (232, 137, 62), (107, 174, 211),
              (243, 237, 241), (114, 83, 59)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
