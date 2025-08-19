from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")
FILE = "data.txt"

def read_highscore():
    with open(FILE) as file:
        highscore = file.read()
    return int(highscore)

def write_highscore(highscore):
    with open(FILE, mode="w") as file:
        file.write(f"{highscore}")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = read_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            write_highscore(self.highscore)
        self.score = 0
        self.update_scoreboard()
