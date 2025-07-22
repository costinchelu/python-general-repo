from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

import os
import traceback


class PasswordManager:

    save_file_location = "../resources/output/passes.json"

    def __init__(self):
        try:
            print(f"Current directory: {os.getcwd()}")

            self.window = Tk()
            self.window.title("Password Manager")
            self.window.config(padx=50, pady=50, )

            self.canvas = Canvas(height=200, width=200)
            self.canvas.grid(row=0, column=1)
            try:
                self.logo_img = PhotoImage(file="../resources/pass_logo.png")
                self.canvas.create_image(100, 100, image=self.logo_img)
                print("Image loaded successfully")
            except Exception as e:
                print(f"Error loading image: {e}")
                self.canvas.create_text(100, 100, text="No Image", fill="black", font=("Arial", 16))


            self.website_label = Label(text="Website:")
            self.email_label = Label(text="Email/Username:")
            self.password_label = Label(text="Password:")
            self.website_label.grid(row=1, column=0)
            self.email_label.grid(row=2, column=0)
            self.password_label.grid(row=3, column=0)

            self.website_entry = Entry(width=25)
            self.email_entry = Entry(width=35)
            self.password_entry = Entry(width=25)
            self.website_entry.grid(row=1, column=1)
            self.website_entry.focus()
            self.email_entry.grid(row=2, column=1, columnspan=2)
            self.email_entry.insert(0, "user@mail.com")
            self.password_entry.grid(row=3, column=1)

            self.generate_password_btn = Button(text="Generate Password", width=16, command=self.generate_password)
            self.add_password_btn = Button(text="Add", width=35, command=self.save_password)
            self.search_entry_btn = Button(text="Search", width=16, command=self.search_entry)
            self.generate_password_btn.grid(row=3, column=2)
            self.add_password_btn.grid(row=4, column=1, columnspan=2)
            self.search_entry_btn.grid(row=1, column=2)
            print("UI setup complete")

        except Exception as e:
            print(f"Error during initialisation: {e}")
            raise

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        pass_letters = [choice(letters) for _ in range(randint(8, 10))]
        pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]

        pass_list = pass_letters + pass_numbers + pass_symbols
        shuffle(pass_list)

        password = "".join(pass_list)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    def save_password(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"You have entered: \nEmail: {email}\nPassword: {password}\nDo you want to save?")

            if is_ok:
                try:
                    with open(self.save_file_location, "r") as file_save:
                        file_data = json.load(file_save)
                except FileNotFoundError:
                    with open(self.save_file_location, "w") as file_save:
                        json.dump(new_data, file_save, indent=4)
                else:
                    file_data.update(new_data)
                    with open(self.save_file_location, "w") as file_save:
                        json.dump(file_data, file_save, indent=4)
                finally:
                    self.website_entry.delete(0, END)
                    self.password_entry.delete(0, END)

    def search_entry(self):
        website = self.website_entry.get()
        try:
            with open(self.save_file_location, "r") as file_save:
                file_data = json.load(file_save)
                try:
                    messagebox.showinfo(title=f"{website}", message=f"User: {file_data[website]['email']}\nPassword: {file_data[website]['password']}")
                except KeyError:
                    messagebox.showinfo(title="No entry in the file", message="Entry not found.")
        except FileNotFoundError:
            messagebox.showinfo(title="No file", message="No entry")

    def run(self):
        self.window.mainloop()


def main():
    print("Starting the password manager...")
    try:
        app = PasswordManager()
        print("Initialization complete, starting main loop")
        app.run()
    except Exception as e:
        print(f"Error in main: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()