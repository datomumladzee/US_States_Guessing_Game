
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 260)


def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {len(guessed_states)}/50",
                       align="center",
                       font=("Arial",16,"bold"))



update_score()

while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title="Guess the state",
        prompt="What's another state's name?"
    )
    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":

        missing_states = []

        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states and answer_state not in guessed_states:

        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        t.color("green")

        state_data = data[data.state == answer_state]

        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

        update_score()

if len(guessed_states) == 50:

    winner = turtle.Turtle()
    winner.hideturtle()
    winner.write("You won!",
                 align="center",
                 font=("Arial",30,"bold"))

turtle.mainloop()