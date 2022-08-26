import random
import pyperclip
from tkinter import *


def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=20)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=80, height=80)
canvas.create_image(40, 40, image=logo)
canvas.grid(column=1, row=1, pady=25)

password_label = Label(text="Password: ", font=("Courier", 15, "normal"))
password_label.grid(column=1, row=2)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", width=10, command=generate_password)
generate_button.focus()
generate_button.grid(column=1, row=4, pady=10)


window.mainloop()
