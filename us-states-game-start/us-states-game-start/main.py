import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
blank = "blank_states_img.gif"
screen.addshape(blank)
turtle.shape(blank)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's the another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

