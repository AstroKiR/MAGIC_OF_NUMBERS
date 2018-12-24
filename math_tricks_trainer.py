#!/usr/bin/env python3

from tkinter import *
from random import randint

root = Tk()

root.title("MathTricksTrainer")
root.minsize(600, 180)

frame_menu = Frame(root, bg="red")
frame_menu.pack(side=TOP, fill=X)

frame_middle= Frame(root, bg="blue")
frame_middle.pack(fill=Y)

frame_bottom = Frame(root)
frame_bottom.pack(side=BOTTOM, fill=X)


# вывод примера
label_1 = Label(frame_middle, text="123456", font=("Arial", 50))
label_1.grid(row=0, column=0)

label_1.configure(text=str(randint(1,100000)))

label_2 = Label(frame_middle, text="+", font=("Arial", 50))
label_2.grid(row=0, column=1)

label_3 = Label(frame_middle, text="654321", font=("Arial", 50))
label_3.grid(row=0, column=2)

label_3.configure(text=str(randint(1,100000)))

# поле ввода ответа
frame_answer = Frame(frame_bottom)
frame_answer.pack(fill=X)

entry_answer = Entry(frame_answer, bg="white", font=("Arial", 20))
entry_answer.grid(sticky="we", row=0, column=0)

button_clear_entry = Button(frame_answer, text="\u2A02",  borderwidth=0)
button_clear_entry.grid(sticky="we", row=0, column=1)

frame_answer.grid_columnconfigure(0, weight=200)
frame_answer.grid_columnconfigure(1, weight=1)


# поле фитбека
frame_feedback = Frame(frame_bottom)
frame_feedback.pack(fill=X)

label_feedback = Label(frame_feedback, text="ENTER YOUR ANSWER", font=("Arial", 20))
label_feedback.pack()


# кнопки
frame_buttons = Frame(frame_bottom)
frame_buttons.pack(fill=X)

frame_buttons.grid_columnconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(1, weight=1)
frame_buttons.grid_columnconfigure(2, weight=1)

btn_1 = Button(frame_buttons, text="NEW")
btn_1.grid(row=1, column=0, sticky="we")

btn_2 = Button(frame_buttons, text="CHECK")
btn_2.grid(row=1, column=1, sticky="we")

btn_3 = Button(frame_buttons, text="ANSWER")
btn_3.grid(row=1, column=2, sticky="we")

root.mainloop()
