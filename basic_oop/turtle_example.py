import random
from turtle import Turtle, Screen

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(tim: Turtle, num_sides: int):
    tim.color(random.choice(colors))
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def get_shapes(tim: Turtle):
    for n in range(3, 11):
        draw_shape(tim, n)

def turtle_example():
    timmy = Turtle()
    my_screen = Screen()

    get_shapes(timmy)
    my_screen.exitonclick()


def main():
    turtle_example()

if __name__ == "__main__":
    main()