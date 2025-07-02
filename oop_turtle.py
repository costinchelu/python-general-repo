from turtle import Turtle, Screen

def main():
    timmy = Turtle()
    print(timmy)
    timmy.shape("turtle")
    timmy.color("DarkOrchid1")
    timmy.forward(100)

    my_screen = Screen()
    print(my_screen.canvheight)

    my_screen.exitonclick()


if __name__ == "__main__":
    main()