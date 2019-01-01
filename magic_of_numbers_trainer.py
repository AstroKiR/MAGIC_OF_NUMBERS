#!/usr/bin/env python3

import configparser

from tkinter import Tk, Frame, Label, Menu, Entry, PhotoImage, Button, Toplevel, Listbox, Spinbox
from tkinter.ttk import Combobox
from random import randint


class TkMathTrickTrainer(Tk):
    ''' Класс обертка 
        самого приложения
    '''     
    def __init__(self, *args, **kwargs):
        ''' Конструктор '''
        Tk.__init__(self, *args, **kwargs)
        self.preference_window = None
        imgicon = PhotoImage(file="calc.png")
        self.tk.call('wm', 'iconphoto', self._w, imgicon)
        self._main_menu()
        self.main_window = MainWindow(self)
        self.main_window.pack()

    def _show_preference_window(self):
        if self.preference_window is None or not self.preference_window.winfo_exists():
            self.preference_window = PreferenceWindow()
        else:
            if self.preference_window.state() == "iconic":
                self.preference_window.state(newstate="normal")
            self.preference_window.lift()
            self.preference_window.focus_force()
            self.preference_window.grab_set()
            self.preference_window.grab_release()

    def _main_menu(self):
        main_menu = Menu(bd=1)
        self.configure(menu=main_menu)
        main_menu.add_command(label="Настройки", font=("Arial", 10), command=lambda: self._show_preference_window())

        
class PreferenceWindow(Toplevel):
    ''' Класс обертка
        окна настройки
    '''
    def __init__(self, *args, **kwargs):
        ''' Конструктор '''
        Toplevel.__init__(self, *args, **kwargs)
        self.wm_title("Настройки")
        self.imgicon = PhotoImage(file="calc.png")
        self.tk.call('wm', 'iconphoto', self._w, self.imgicon)
        self._show_fields()
        self._get_preferences()

    def _show_fields(self):
        ''' Метод формирования полей окна с настройками '''

        # верхний фрейм
        tl_top_frame = Frame(self)
        tl_top_frame.pack(side="top")

        # нижний фрейм
        tl_bottom_frame = Frame(self)
        tl_bottom_frame.pack(side="bottom")

        tl_label_n1 = Label(tl_top_frame, text="first number: ")
        tl_label_n1.grid(row=0, column=0)

        # блок 1-го числа С
        tl_label_n11 = Label(tl_top_frame, text="from")
        tl_label_n11.grid(row=0, column=1)
        self.spinbox_n11 = Spinbox(tl_top_frame, from_=0, to=1000000000)
        self.spinbox_n11.grid(row=0, column=2)

        # блок 1-го числа ПО
        tl_label_n12 = Label(tl_top_frame, text="to")
        tl_label_n12.grid(row=0, column=3)
        self.spinbox_n12 = Spinbox(tl_top_frame, from_=0, to=1000000000)
        self.spinbox_n12.grid(row=0, column=4)

        tl_label_n2 = Label(tl_top_frame, text="second number: ")
        tl_label_n2.grid(row=1, column=0, sticky='ew')

        # блок 2-го числа С
        tl_label_n21 = Label(tl_top_frame, text="from")
        tl_label_n21.grid(row=1, column=1, sticky='ew')
        self.spinbox_n21 = Spinbox(tl_top_frame, from_=0, to=1000000000)
        self.spinbox_n21.grid(row=1, column=2, sticky='ew')

        # блок 2-го числа ПО
        tl_label_n22 = Label(tl_top_frame, text="to")
        tl_label_n22.grid(row=1, column=3, sticky='ew')
        self.spinbox_n22 = Spinbox(tl_top_frame, from_=0, to=1000000000)
        self.spinbox_n22.grid(row=1, column=4, sticky='ew')
        
        # блок с математическими операциями
        tl_combobox_label = Label(tl_top_frame, text="select math operation: ")
        tl_combobox_label.grid(row=2, column=0, sticky='ew')
        list_math_operations = [
            "Сумма (+)",
            "Разность (-)",
            "Умножение (*)",
            "Деление (/)",
            "Возведение в степень (^)"
        ]
        self.combobox_math_operation = Combobox(tl_top_frame, values=list_math_operations)
        self.combobox_math_operation.grid(row=2, column=1, columnspan=4, sticky="ew")
        self.combobox_math_operation.current(0)

        # кнопка Сохранить
        tl_save_cencel = Button(tl_bottom_frame, text="Save", width=10, command=lambda: self._set_preferences())
        tl_save_cencel.grid(row=0, column=0)

        # кнопка Закрыть
        tl_button_cencel = Button(tl_bottom_frame, text="Cencel", width=10, command=lambda: self.destroy())
        tl_button_cencel.grid(row=0, column=1)

    def _get_preferences(self):
        config = configparser.ConfigParser()
        config.read("magic.conf")

        self.spinbox_n11.delete(0, "end")
        self.spinbox_n11.insert(0, config["MAGIC"]["first_number_from"])

        self.spinbox_n12.delete(0, "end")
        self.spinbox_n12.insert(0, config["MAGIC"]["first_number_to"])

        self.spinbox_n21.delete(0, "end")
        self.spinbox_n21.insert(0, config["MAGIC"]["second_number_from"])

        self.spinbox_n22.delete(0, "end")
        self.spinbox_n22.insert(0, config["MAGIC"]["second_number_to"])

        self.combobox_math_operation.delete(0, "end")
        if config["MAGIC"]["math_operation"] == '1':
            self.combobox_math_operation.insert(0, "Сумма (+)")
        elif config["MAGIC"]["math_operation"] == '2':
            self.combobox_math_operation.insert(0, "Разность (-)")
        elif config["MAGIC"]["math_operation"] == '3':
            self.combobox_math_operation.insert(0, "Умножение (*)")
        elif config["MAGIC"]["math_operation"] == '4':
            self.combobox_math_operation.insert(0, "Деление (/)")
        elif config["MAGIC"]["math_operation"] == '5':
            self.combobox_math_operation.insert(0, "Возведение в степень (^)")
        else:
            self.combobox_math_operation.insert(0, "Сумма (+)")

    def _set_preferences(self):
        path = "./magic.conf"
        config = configparser.ConfigParser()
        config.read(path)

        if self.spinbox_n11.get().isdigit():
            config.set("MAGIC", "first_number_from", self.spinbox_n11.get())
        if self.spinbox_n12.get().isdigit():
            config.set("MAGIC", "first_number_to", self.spinbox_n12.get())
        if self.spinbox_n21.get().isdigit():
            config.set("MAGIC", "second_number_from", self.spinbox_n21.get())
        if self.spinbox_n22.get().isdigit():
            config.set("MAGIC", "second_number_to", self.spinbox_n22.get())

        if self.combobox_math_operation.get() == "Сумма (+)":
            config.set("MAGIC", "math_operation", '1')
        elif self.combobox_math_operation.get() == "Разность (-)":
            config.set("MAGIC", "math_operation", '2')
        elif self.combobox_math_operation.get() == "Умножение (*)":
            config.set("MAGIC", "math_operation", '3')
        elif self.combobox_math_operation.get() == "Деление (/)":
            config.set("MAGIC", "math_operation", '4')
        elif self.combobox_math_operation.get() == "Возведение в степень (^)":
            config.set("MAGIC", "math_operation", '5')

        with open(path, "w") as config_file:
            config.write(config_file)

        self._get_preferences()


class MainWindow(Frame):
    ''' Класс описывает
        главное окно приложения
    '''
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
        btn_1 = Button(bottom_frame, text="NEW", command=self.generate_question)
        btn_1.grid(row=1, column=0, sticky="we")
        btn_2 = Button(bottom_frame, text="CHECK", command=self.check_answer)
        btn_2.grid(row=1, column=1, sticky="we")
        btn_3 = Button(bottom_frame, text="ANSWER", command=self.get_answer)
        btn_3.grid(row=1, column=2, sticky="we")

    def generate_question(self):
        self.get_config()
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
    


if __name__ == "__main__":
    root = TkMathTrickTrainer()
    root.title("Счет в уме")
    root.minsize(600, 180)
    root.mainloop()

