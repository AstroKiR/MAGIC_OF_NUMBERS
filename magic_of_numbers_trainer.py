#!/usr/bin/env python3

import os
from tkinter import * 
from random import randint


class MainWindow(Frame):


    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.n1 = 0
        self.n2 = 0
        self.math_operation = "+"

        self.question_block()
        self.note_block()
        self.answer_block()
        self.button_block()


    def question_block(self):
        self.question_frame = Frame(self, bg="red")
        self.question_frame.pack(side="top", fill="y")
        self.label_1 = Label(self.question_frame, font=("Arial", 50))
        self.label_1.grid(row=0, column=0)
        self.label_2 = Label(self.question_frame, text="+", font=("Arial", 50))
        self.label_2.grid(row=0, column=1)
        self.label_3 = Label(self.question_frame, font=("Arial", 50))
        self.label_3.grid(row=0, column=2)


    def note_block(self):
        self.note_frame = Frame(self, bg="blue")
        self.note_frame.pack()
        self.label_feedback = Label(self.note_frame, text="ENTER YOUR ANSWER", font=("Arial", 20), fg="#838384")
        self.label_feedback.pack()


    def answer_block(self):
        self.answer_frame = Frame(self)
        self.answer_frame.pack(padx=5, pady=10)
        self.entry_answer = Entry(self.answer_frame, bg="white", font=("Arial", 20), width=10)
        self.entry_answer.grid(sticky="we", row=0, column=0)
        self.button_clear_entry = Button(self.answer_frame, text="\u2A02", borderwidth=0, font=("Arial", 13), fg="#838384")
        self.button_clear_entry.grid(sticky="we", row=0, column=1)
        self.button_clear_entry.bind("<Button-1>", self.clear_entry)
        self.answer_frame.grid_columnconfigure(0, weight=200)
        self.answer_frame.grid_columnconfigure(1, weight=1)


    def button_block(self):
        self.bottom_frame = Frame(self, bg="green")
        self.bottom_frame.pack(side="bottom", fill="x")

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_columnconfigure(2, weight=1)

        self.btn_1 = Button(self.bottom_frame, text="NEW", font=("Arial", 16), fg="#838384")
        self.btn_1.grid(row=1, column=0, sticky="we")
        self.btn_1.bind("<Button-1>", self.generate_question)

        self.btn_2 = Button(self.bottom_frame, text="CHECK", font=("Arial", 16), fg="#838384")
        self.btn_2.grid(row=1, column=1, sticky="we")
        self.btn_2.bind("<Button-1>", self.check_answer)

        self.btn_3 = Button(self.bottom_frame, text="ANSWER", font=("Arial", 16), fg="#838384")
        self.btn_3.grid(row=1, column=2, sticky="we")
        self.btn_3.bind("<Button-1>", self.get_answer)


    def generate_question(self, event):
        self.n1 = randint(10,100)
        self.n2 = randint(10,100)
        self.label_1.configure(text=str(self.n1))
        self.label_3.configure(text=str(self.n2))
        self.label_feedback.configure(text="ENTER YOUR ANSWER", fg="#838384")
        self.entry_answer.delete(0, "end")
    

    def check_answer(self, event):
        user_answer = self.entry_answer.get()
        true_answer = self.n1 + self.n2
        if user_answer == str(true_answer):
            self.label_feedback.configure(text="TRUE", fg="green")
        else:
            self.label_feedback.configure(text="FALSE", fg="red")


    def get_answer(self, event):
        answer = self.n1 + self.n2
        self.label_feedback.configure(text=str(answer), fg="#838384")


    def clear_entry(self, event):
        self.entry_answer.delete(0, "end")


def show_config_window(parent):
    t = Toplevel(parent)
    t.wm_title("Math tricks trainer settimns")
    imgicon = PhotoImage(file="calc.png")
    t.tk.call('wm', 'iconphoto', t._w, imgicon)  
    l = Label(t, text="This is window")
    l.pack(side="top", fill="both", expand=True, padx=100, pady=100)


if __name__ == "__main__":
    root = Tk()
    root.title("MathTricksTrainer")
    root.minsize(600, 180)
    
    imgicon = PhotoImage(file="calc.png")
    root.tk.call('wm', 'iconphoto', root._w, imgicon)  
    
    main_menu = Menu(bd=0)

    root.configure(menu=main_menu, background="#000000")

    main_menu.add_command(
            label="\u2699", 
            font=("Arial", 15), 
            command=lambda:show_config_window(root))

    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)

    root.mainloop()

