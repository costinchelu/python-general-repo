from tkinter import *
import pandas
import random

class FlashCard:

    BACKGROUND_COLOR = "#B1DDC6"
    IMG_CARD_BACK = "../resources/flash_card_img/card_back.png"
    IMG_CARD_FRONT = "../resources/flash_card_img/card_front.png"
    IMG_RIGHT = "../resources/flash_card_img/right.png"
    IMG_WRONG = "../resources/flash_card_img/wrong.png"
    WORDS = "../resources/french_words.csv"
    TO_LEARN_FILE = "../resources/output/flash_card_to_learn.csv"
    current_card = {}

    def __init__(self):
        try:
            self.file_df = pandas.read_csv(self.TO_LEARN_FILE)
        except FileNotFoundError:
            self.file_df = pandas.read_csv(self.WORDS)
        self.data_dict = self.file_df.to_dict(orient="records")

        self.window = Tk()
        self.window.title("Flashcards")
        self.window.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)

        self.flip_timer = self.window.after(3000, func=self.flip_card)

        self.card_front_img = PhotoImage(file=self.IMG_CARD_FRONT)
        self.card_back_img = PhotoImage(file=self.IMG_CARD_BACK)
        self.cross_image = PhotoImage(file=self.IMG_WRONG)
        self.check_image = PhotoImage(file=self.IMG_RIGHT)

        self.canvas = Canvas(width=800, height=526)
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.config(bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.unknown_btn = Button(image=self.cross_image, highlightthickness=0, command=self.next_card)
        self.known_btn = Button(image=self.check_image, highlightthickness=0, command=self.is_known)
        self.unknown_btn.grid(row=1, column=0)
        self.known_btn.grid(row=1, column=1)

        self.next_card()


    def next_card(self):
        self.window.after_cancel(self.flip_timer)

        self.current_card = random.choice(self.data_dict)

        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_card["French"], fill="black")
        self.canvas.itemconfig(self.card_background, image=self.card_front_img)

        self.flip_timer = self.window.after(3000, func=self.flip_card)


    def flip_card(self):
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_card["English"], fill="white")
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)


    def is_known(self):
        self.data_dict.remove(self.current_card)

        data_to_save_df = pandas.DataFrame(self.data_dict)
        data_to_save_df.to_csv(self.TO_LEARN_FILE, index=False)

        self.next_card()


    def run(self):
        self.window.mainloop ()


def main():
    app = FlashCard()
    app.run()


if __name__ == "__main__":
    main()