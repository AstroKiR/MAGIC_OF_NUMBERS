#!/usr/bin/env python3

import configparser

from tkinter import Tk, Frame, Label, Menu, Entry, PhotoImage, Button, Toplevel, Listbox
from tkinter.ttk import Combobox
from random import randint


class MainWindow(Frame):
    """ 
        Class of main window
    """
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.n1_conf = [0, 0] 
        self.n2_conf = [0, 0]
        self.n1 = 0 
        self.n2 = 0
        self.math_operation_conf = 1 
        self.question_block()
        self.note_block()
        self.answer_block()
        self.button_block()
        self.get_config()
        self.generate_question()

    def get_config(self):
        config = configparser.ConfigParser()
        config.read("magic.conf")
        self.n1_conf[0] = int(config["MAGIC"]["first_number_from"])
        self.n1_conf[1] = int(config["MAGIC"]["first_number_to"])
        self.n2_conf[0] = int(config["MAGIC"]["second_number_from"])
        self.n2_conf[1] = int(config["MAGIC"]["second_number_to"])
        self.math_operation_conf = int(config["MAGIC"]["math_operation"])

    def question_block(self):
        question_frame = Frame(self)
        question_frame.pack(side="top", fill="y")
        self.string_with_question = Label(question_frame, font=("Arial", 50))
        self.string_with_question.grid(row=0, column=0)

    def note_block(self):
        note_frame = Frame(self, bg="blue")
        note_frame.pack()
        self.label_feedback = Label(note_frame, text="ENTER YOUR ANSWER", font=("Arial", 20), fg="#838384")
        self.label_feedback.pack()

    def answer_block(self):
        answer_frame = Frame(self)
        answer_frame.pack(padx=5, pady=10)
        self.entry_answer = Entry(answer_frame)
        self.entry_answer.config(bg="white", font=("Arial", 20), width=10)
        self.entry_answer.grid(sticky="we", row=0, column=0)
        button_clear_entry = Button(answer_frame, text="\u2A02")
        button_clear_entry.config(borderwidth=0, font=("Arial", 13), fg="#838384")
        button_clear_entry.grid(sticky="we", row=0, column=1)
        button_clear_entry.bind("<Button-1>", self.clear_entry)
        answer_frame.grid_columnconfigure(0, weight=200)
        answer_frame.grid_columnconfigure(1, weight=1)

    def button_block(self):
        bottom_frame = Frame(self, bg="green")
        bottom_frame.pack(side="bottom", fill="x")
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)
        bottom_frame.grid_columnconfigure(2, weight=1)
        btn_1 = Button(bottom_frame, text="NEW", font=("Arial", 16), fg="#838384", 
                command=self.generate_question)
        btn_1.grid(row=1, column=0, sticky="we")
        btn_2 = Button(bottom_frame, text="CHECK", font=("Arial", 16), fg="#838384",
                command=self.check_answer)
        btn_2.grid(row=1, column=1, sticky="we")
        btn_3 = Button(bottom_frame, text="ANSWER", font=("Arial", 16), fg="#838384",
                command=self.get_answer)
        btn_3.grid(row=1, column=2, sticky="we")

    def generate_question(self):
        self.n1 = randint(self.n1_conf[0], self.n1_conf[1])
        self.n2 = randint(self.n2_conf[0], self.n2_conf[1])
        if self.math_operation_conf == 1:
            mo = "+"
        elif self.math_operation_conf == 2:
            mo = "-"
        elif self.math_operation_conf == 3:
            mo = "*"
        elif self.math_operation_conf == 4:
            mo = "/"
        elif self.math_operation_conf == 5:
            mo = "^"
        self.string_with_question.config(text="{} {} {}".format(self.n1, mo, self.n2))
        self.label_feedback.config(text="ENTER YOUR ANSWER", fg="#838384")
        self.entry_answer.delete(0, "end")

    def check_answer(self):
        user_answer = self.entry_answer.get()

        if self.math_operation_conf == 1:
            true_answer = self.n1 + self.n2
        elif self.math_operation_conf == 2:
            true_answer = self.n1 - self.n2
        elif self.math_operation_conf == 3:
            true_answer = self.n1 * self.n2
        elif self.math_operation_conf == 4:
            true_answer = self.n1 / self.n2
        elif self.math_operation_conf == 5:
            true_answer = self.n1 ** self.n2

        if user_answer == str(true_answer):
            self.label_feedback.config(text="TRUE", fg="green")
        else:
            self.label_feedback.config(text="FALSE", fg="red")

    def get_answer(self):
        if self.math_operation_conf == 1:
            true_answer = self.n1 + self.n2
        elif self.math_operation_conf == 2:
            true_answer = self.n1 - self.n2
        elif self.math_operation_conf == 3:
            true_answer = self.n1 * self.n2
        elif self.math_operation_conf == 4:
            true_answer = self.n1 / self.n2
        elif self.math_operation_conf == 5:
            true_answer = self.n1 ** self.n2

        self.label_feedback.config(text=str(true_answer), fg="#838384")

    def clear_entry(self, event):
        self.entry_answer.delete(0, "end")


def show_config_window(parent):
    tl_window = Toplevel(parent)
    tl_window.wm_title("Math tricks trainer settimns")
    imgicon = PhotoImage(file="calc.png")
    tl_window.tk.call('wm', 'iconphoto', tl_window._w, imgicon)

    tl_top_frame = Frame(tl_window)
    tl_top_frame.pack(side="top")

    tl_bottom_frame = Frame(tl_window)
    tl_bottom_frame.pack(side="bottom")

    tl_label_n1 = Label(tl_top_frame, text="first number: ")
    tl_label_n1.grid(row=0, column=0)

    tl_label_n11 = Label(tl_top_frame, text="from")
    tl_label_n11.grid(row=0, column=1)
    tl_entry_n11 = Entry(tl_top_frame, width=20)
    tl_entry_n11.grid(row=0, column=2)

    tl_label_n12 = Label(tl_top_frame, text="to")
    tl_label_n12.grid(row=0, column=3)
    tl_entry_n12 = Entry(tl_top_frame, width=20)
    tl_entry_n12.grid(row=0, column=4)


    tl_label_n2 = Label(tl_top_frame, text="second number: ")
    tl_label_n2.grid(row=1, column=0, sticky='ew')

    tl_label_n21 = Label(tl_top_frame, text="from")
    tl_label_n21.grid(row=1, column=1, sticky='ew')
    tl_entry_n21 = Entry(tl_top_frame, width=20)
    tl_entry_n21.grid(row=1, column=2, sticky='ew')

    tl_label_n22 = Label(tl_top_frame, text="to")
    tl_label_n22.grid(row=1, column=3, sticky='ew')
    tl_entry_n22 = Entry(tl_top_frame, width=20)
    tl_entry_n22.grid(row=1, column=4, sticky='ew')

    tl_combobox_label = Label(tl_top_frame, text="select math operation: ")
    tl_combobox_label.grid(row=2, column=0, sticky='ew')
    list_math_operations = ["Сумма (+)", "Разность (-)", "Умножение (*)", "Деление (/)", "Возведение в степень (^)"]
    tl_combobox_math_operation = Combobox(tl_top_frame, values=list_math_operations)
    tl_combobox_math_operation.grid(row=2, column=1, columnspan=4, sticky="ew")
    tl_combobox_math_operation.current(0)

    tl_save_cencel = Button(tl_bottom_frame, text="Save", width=10)
    tl_save_cencel.grid(row=0, column=0) 
    tl_button_cencel = Button(tl_bottom_frame, text="Cencel", width=10, command=lambda: tl_window.destroy())
    tl_button_cencel.grid(row=0, column=1) 


if __name__ == "__main__":
    root = Tk()
    root.title("MathTricksTrainer")
    root.minsize(600, 180)

    imgicon = PhotoImage(file="calc.png")
    root.tk.call('wm', 'iconphoto', root._w, imgicon)

    main_menu = Menu(bd=1)

    root.configure(menu=main_menu, background="#000000")

    main_menu.add_command(
            label="\u2699",
            font=("Arial", 15),
            command=lambda: show_config_window(root))

    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)

    root.mainloop()
