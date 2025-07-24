from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
IMG_FALSE = "../../resources/flash_card_img/wrong.png"
IMG_TRUE = "../../resources/flash_card_img/right.png"


class QuizzInterface:

    def __init__(self, quiz_brain = QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_image = PhotoImage(file=IMG_TRUE)
        false_image = PhotoImage(file=IMG_FALSE)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, sticky="e")

        self.canvas = Canvas(width=400, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_btn = Button(image=true_image, highlightthickness=0)
        self.false_btn = Button(image=false_image, highlightthickness=0)
        self.true_btn.grid(row=2, column=0, sticky="w")
        self.false_btn.grid(row=2, column=1, sticky="e")

        self.window.mainloop()

    # def get_next_