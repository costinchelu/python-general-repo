from tkinter import *


def main():
    window = Tk()
    window.title("GUI Demo 1")
    window.minsize(width=500, height=300)
    window.config(padx=20, pady=20)

    label1 = Label(text="Old text", font=("Arial", 24, "bold"))
    # label1.place(x=0, y=0)
    # label1.pack()
    label1.grid(column=0, row=0)

    # change the configuration of an object:
    label1["text"] = "One way to change object configuration"
    label1.config(text="Label 1", font=("Arial", 20))

    def button1_clicked():
        label1.config(text="I got clicked")
        print("I got clicked")

    button1 = Button(text="Click Me", command=button1_clicked)
    button1.grid(column=1, row=0)

    input1 = Entry(width=30)
    input1.insert(END, string="Some text to begin with.")
    # Gets text in entry
    print(input1.get())
    input1.grid(column=0, row=1)


    text = Text(height=5, width=30)
    # Puts cursor in textbox.
    text.focus()
    # Adds some text to begin with.
    text.insert(END, "Example of multi-line text entry.")
    # Get's current value in textbox at line 1, character 0
    print(text.get("1.0", END))
    text.grid(column=1, row=1)


    def spinbox_used():
        # gets the current value in spinbox.
        print(spinbox.get())

    spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
    spinbox.grid(column=0, row=2)

    # Scale (called with current scale value)
    def scale_used(value):
        print(value)

    scale = Scale(from_=0, to=100, command=scale_used)
    scale.grid(column=3, row=2)


    def checkbutton_used():
        # Prints 1 if On button checked, otherwise 0.
        print(checked_state.get())

    # variable to hold on to checked state, 0 is off, 1 is on.
    checked_state = IntVar()
    checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
    checked_state.get()
    checkbutton.grid(column=0, row=3)


    def radio_used():
        print(radio_state.get())

    # Variable to hold on to which radio button value is checked.
    radio_state = IntVar()
    radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
    radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
    radiobutton1.grid(column=0, row=4)
    radiobutton2.grid(column=1, row=4)


    def listbox_used(event):
        # Gets current selection from listbox
        print(listbox.get(listbox.curselection()))

    listbox = Listbox(height=4)
    fruits = ["Apple", "Pear", "Orange", "Banana"]
    for item in fruits:
        listbox.insert(fruits.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.grid(column=1, row=5)

    window.mainloop()


if __name__ == "__main__":
    main()

