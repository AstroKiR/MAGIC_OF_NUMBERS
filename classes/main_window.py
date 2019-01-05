import configparser


from tkinter import Button, Entry, Frame, Label
from random import randint


class MAIN_WINDOW(Frame):
    """ Класс описывает главное окно приложения """

    def __init__(self, *args, **kwargs):
        ''' Конструктор '''
        Frame.__init__(self, *args, **kwargs)
        self.n1_conf = [0, 0]
        self.n2_conf = [0, 0]
        self.n1 = 0
        self.n2 = 0
        self._math_operation_conf = 1
        self._question_block()
        self._note_block()
        self._answer_block()
        self._button_block()
        self._get_config()
        self._generate_question()

    def _get_config(self):
        ''' Метод получния настроек из конфигурационного файла '''
        config = configparser.ConfigParser()
        config.read("magic.conf")
        self.n1_conf[0] = int(config["MAGIC"]["first_number_from"])
        self.n1_conf[1] = int(config["MAGIC"]["first_number_to"])
        self.n2_conf[0] = int(config["MAGIC"]["second_number_from"])
        self.n2_conf[1] = int(config["MAGIC"]["second_number_to"])
        self.math_operation_conf = int(config["MAGIC"]["math_operation"])

    def _question_block(self):
        ''' Метод отрисовывает блок с примером '''
        question_frame = Frame(self)
        question_frame.pack(side="top", fill="y")
        self.string_with_question = Label(question_frame)
        self.string_with_question.grid(row=0, column=0)

    def _note_block(self):
        ''' Метод отрисовывает блок с информацией '''
        note_frame = Frame(self, bg="blue")
        note_frame.pack()
        self.label_feedback = Label(note_frame, text="ENTER YOUR ANSWER")
        self.label_feedback.pack()

    def _answer_block(self):
        ''' Метод отрисовывает блок вводи ответа '''
        answer_frame = Frame(self)
        answer_frame.pack(padx=5, pady=10)
        self.entry_answer = Entry(answer_frame)
        self.entry_answer.config(bg="white")
        self.entry_answer.grid(sticky="we", row=0, column=0)
        button_clear_entry = Button(answer_frame, text="\u2A02")
        button_clear_entry.config(borderwidth=0)
        button_clear_entry.grid(sticky="we", row=0, column=1)
        button_clear_entry.bind("<Button-1>", self.clear_entry)
        answer_frame.grid_columnconfigure(0, weight=200)
        answer_frame.grid_columnconfigure(1, weight=1)

    def _button_block(self):
        ''' Метод отрисовывает кнопки '''
        bottom_frame = Frame(self, bg="green")
        bottom_frame.pack(side="bottom", fill="x")
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)
        bottom_frame.grid_columnconfigure(2, weight=1)
        btn_1 = Button(bottom_frame, text="Новый", command=self._generate_question)
        btn_1.grid(row=1, column=0, sticky="we")
        btn_2 = Button(bottom_frame, text="Проверить", command=self.check_answer)
        btn_2.grid(row=1, column=1, sticky="we")
        btn_3 = Button(bottom_frame, text="Ответ", command=self.get_answer)
        btn_3.grid(row=1, column=2, sticky="we")

    def _generate_question(self):
        ''' Метод генерирует новый пример (вопрос) '''
        self._get_config()
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
        self.label_feedback.config(text="Ведите свой ответ", fg="#838384")
        self.entry_answer.delete(0, "end")

    def check_answer(self):
        ''' Метод проверяер ответ пользователя '''
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
        ''' Метод вывод правильный ответ '''
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
        ''' Метод очищает поле с ответом пользователя '''
        self.entry_answer.delete(0, "end")
