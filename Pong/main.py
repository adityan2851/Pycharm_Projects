from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

right = Paddle((350, 0))
left = Paddle((-350, 0))


screen.listen()
screen.onkey(right.go_up, "Up")
screen.onkey(right.go_down, "Down")
screen.onkey(left.go_up, "w")
screen.onkey(left.go_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.xcor() > 300 or ball.ycor() < -300:
        ball.bounce()

screen.exitonclick()
