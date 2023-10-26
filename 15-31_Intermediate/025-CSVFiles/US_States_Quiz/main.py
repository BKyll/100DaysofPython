import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(720, 500)
image = "025-CSVFiles/US_States_Quiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.pu()
WRITER_ALIGN = "center"
WRITER_FONT = ("Courier", 8, "normal")

writer.goto(-165, 225)
writer.write('"Exit" to quit.', align=WRITER_ALIGN, font=WRITER_FONT)

# # Getting state x, y coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

states = pandas.read_csv("025-CSVFiles/US_States_Quiz/50_states.csv")
correct_guesses = 0
states_guessed = []


def add_label(state):
    state_coor = states[states.state == f"{state}"]
    writer.goto(int(state_coor['x']), int(state_coor['y']))
    writer.write(f"{state}", align=WRITER_ALIGN, font=WRITER_FONT)


while correct_guesses != len(states.state):
    user_guess = screen.textinput(title=f"{correct_guesses}/{len(states.state)} States Correct",
                                  prompt="Guess another state!").title()
    if user_guess == "Exit":
        # Day 26 Update with List Comprehension
        # Old
        # states_to_learn = []
        # for s in states.state:
        #     if s not in states_guessed:
        #         states_to_learn.append(s)
        states_to_learn = [s for s in states.state if s not in states_guessed]
        stl = pandas.DataFrame(states_to_learn, columns=["state"])
        stl.to_csv("025-CSVFiles/US_States_Quiz/states_to_learn.csv")
        break

    if user_guess not in states_guessed:
        if user_guess in states.state.values:
            correct_guesses += 1
            states_guessed.append(user_guess)
            add_label(user_guess)
