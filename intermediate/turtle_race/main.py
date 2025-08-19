from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win? Choose:\nred\norange\nyellow\ngreen\nblue\nindigo\ndarkviolet"
)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "darkviolet"]
turtles = []
Y_POSITION_STARTER = -150
X_POSITION = -230
is_race_on = False

for t in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x=X_POSITION, y=Y_POSITION_STARTER + t * 50)
    new_turtle.showturtle()
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won with {winning_color}")
            else:
                print(f"You lost! {winning_color} won")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()