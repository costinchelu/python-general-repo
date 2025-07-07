# from turtle import Turtle, Screen
import random
import turtle as t
import colorgram as c

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

image = '../resources/hirst-dots.jpeg'


colors_2 = [(233, 233, 232), (231, 233, 237), (236, 232, 234), (222, 232, 225), (208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 83), (168, 160, 39), (128, 189, 143), (83, 20, 44), (38, 42, 67), (186, 93, 106), (187, 140, 170), (84, 122, 181), (59, 39, 31), (79, 153, 165), (88, 157, 91), (194, 79, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (58, 130, 122), (217, 176, 187), (220, 182, 167), (166, 207, 164), (179, 188, 211), (148, 37, 35), (46, 73, 71), (46, 65, 62)]


def get_colors_from_image(img: str):
    extracted_colors = c.extract(img, 34)
    image_colors = []
    for cl in extracted_colors:
        color = cl.rgb
        image_colors.append((color.r, color.g, color.b))
    return image_colors


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def draw_shape(tim: t.Turtle, num_sides: int):
    tim.color(random.choice(colors))
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def get_shapes(tim: t.Turtle):
    for n in range(3, 11):
        draw_shape(tim, n)


def random_walk(tim: t.Turtle):
    tim.pensize(12)
    for _ in range(400):
        tim.color(random_color())
        tim.setheading(random.choice([0, 90, 180, 270]))
        tim.forward(30)


def draw_spiro(tim: t.Turtle, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(200)
        tim.setheading(tim.heading() + size_of_gap)


def draw_hears_dots(tim: t.Turtle):
    # color_list = get_colors_from_image(image)
    tim.penup()
    tim.setheading(225)
    tim.forward(500)
    tim.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        tim.dot(40, random.choice(colors_2))
        tim.forward(80)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(80)
            tim.setheading(180)
            tim.forward(800)
            tim.setheading(0)


def turtle_example():
    t.colormode(255)
    timmy = t.Turtle()
    timmy.speed("fastest")
    timmy.hideturtle()
    my_screen = t.Screen()
    my_screen.bgcolor("black")

    # user_choice = input("Choose: \n1 for shapes, \n2 for random walk, \n3 for spirograph \n4 for Hearst painting\n ")
    # if user_choice == "1":
    #     get_shapes(timmy)
    # elif user_choice == "2":
    #     random_walk(timmy)
    # elif user_choice == "3":
    #     draw_spiro(timmy, 3)
    # else:
    #     my_screen.bgcolor("white")
    #     draw_hears_dots(timmy)
    my_screen.bgcolor("white")
    draw_hears_dots(timmy)

    my_screen.exitonclick()


def main():
    turtle_example()


if __name__ == "__main__":
    main()
