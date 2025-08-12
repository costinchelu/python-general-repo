import turtle
import pandas

IMAGE_FILE = "../resources/blank_states_img.gif"
DATA_FILE = "../resources/50_states.csv"
OUTPUT_FILE = "../resources/output/states_to_learn.csv"

def program():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(IMAGE_FILE)
    turtle.shape(IMAGE_FILE)

    data = pandas.read_csv(DATA_FILE)
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer = (screen.textinput(
            title=f"{len(guessed_states)}/50 States Correct",
            prompt="What's another state's name?"
        ).title())

        if answer == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            output_data = pandas.DataFrame(missing_states)
            output_data.to_csv(OUTPUT_FILE)
            break

        if answer in all_states:
            guessed_states.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer)


def main():
    program()

if __name__ == "__main__":
    main()