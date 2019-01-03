
import configparser
import re

from tkinter import Button, Entry, Frame, Label, PhotoImage, Toplevel
from tkinter.ttk import Combobox


class PREFERENCE_WINDOW(Toplevel):
    """ Класс обертка окна настройки """

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

        validate_entry_field = (self.register(self._local_validate_entry), "%i", "%P", "%S")

        # блок 1-го числа С
        tl_label_n11 = Label(tl_top_frame, text="from")
        tl_label_n11.grid(row=0, column=1)
        self.entry_n11 = Entry(tl_top_frame, validate="key", validatecommand=validate_entry_field)
        self.entry_n11.grid(row=0, column=2)

        # блок 1-го числа ПО
        tl_label_n12 = Label(tl_top_frame, text="to")
        tl_label_n12.grid(row=0, column=3)
        self.entry_n12 = Entry(tl_top_frame, validate="key", validatecommand=validate_entry_field)
        self.entry_n12.grid(row=0, column=4)

        tl_label_n2 = Label(tl_top_frame, text="second number: ")
        tl_label_n2.grid(row=1, column=0, sticky='ew')

        # блок 2-го числа С
        tl_label_n21 = Label(tl_top_frame, text="from")
        tl_label_n21.grid(row=1, column=1, sticky='ew')
        self.entry_n21 = Entry(tl_top_frame, validate="key", validatecommand=validate_entry_field)
        self.entry_n21.grid(row=1, column=2, sticky='ew')

        # блок 2-го числа ПО
        tl_label_n22 = Label(tl_top_frame, text="to")
        tl_label_n22.grid(row=1, column=3, sticky='ew')
        self.entry_n22 = Entry(tl_top_frame, validate="key", validatecommand=validate_entry_field)
        self.entry_n22.grid(row=1, column=4, sticky='ew')
        
        # блок с математическими операциями
         
        validate_combobox_field = (self.register(self._local_validate_combobox), "%i", "%P", "%S")

        tl_combobox_label = Label(tl_top_frame, text="select math operation: ")
        tl_combobox_label.grid(row=2, column=0, sticky='ew')

        list_math_operations = [
            "Сумма (+)",
            "Разность (-)",
            "Умножение (*)",
            "Деление (/)",
            "Возведение в степень (^)"
        ]

        self.combobox_math_operation = Combobox(
                tl_top_frame, 
                values=list_math_operations, 
                validate="all",
                validatecommand=validate_combobox_field
        )

        self.combobox_math_operation.grid(row=2, column=1, columnspan=4, sticky="ew")
        self.combobox_math_operation.current(0)

        self.tl_info_label = Label(tl_top_frame, text="")
        self.tl_info_label.grid(row=3, column=0, columnspan=5)

        # кнопка Сохранить
        tl_save_cencel = Button(tl_bottom_frame, text="Save", width=10, command=lambda: self._set_preferences())
        tl_save_cencel.grid(row=0, column=0)

        # кнопка Закрыть
        tl_button_cencel = Button(tl_bottom_frame, text="Cencel", width=10, command=lambda: self.destroy())
        tl_button_cencel.grid(row=0, column=1)

    def _get_preferences(self):
        ''' Метод считывает файла magic.conf и заполняет поля при открытии окна настроек '''

        # данные из magic.conf
        config = configparser.ConfigParser()
        config.read("magic.conf")
        
        # наполнение полей текущими данными
        self.entry_n11.delete(0, "end")
        self.entry_n11.insert(0, config["MAGIC"]["first_number_from"])
        self.entry_n12.delete(0, "end")
        self.entry_n12.insert(0, config["MAGIC"]["first_number_to"])
        self.entry_n21.delete(0, "end")
        self.entry_n21.insert(0, config["MAGIC"]["second_number_from"])
        self.entry_n22.delete(0, "end")
        self.entry_n22.insert(0, config["MAGIC"]["second_number_to"])
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
        ''' Метод сохраняет новые настройки в файл magic.conf '''

        if self._total_validate_fields():

            path = "./magic.conf"
            config = configparser.ConfigParser()
            config.read(path)

            config.set("MAGIC", "first_number_from", self.entry_n11.get())
            config.set("MAGIC", "first_number_to", self.entry_n12.get())
            config.set("MAGIC", "second_number_from", self.entry_n21.get())
            config.set("MAGIC", "second_number_to", self.entry_n22.get())

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

    def _local_validate_entry(self, i, P, S):
        ''' Метод локально валидирует текстовое поле при вводе символов '''
        if re.match("[-+]?\d*$", P) or P == '':
            return True
        else:
            return False

    def _local_validate_combobox(self, i, P, S):
        ''' Метод локально валидирует комбобокс, 
            точнее дает выбрать только значения из выпадающео списка
        '''
        if P in ["Сумма (+)", "Разность (-)","Умножение (*)","Деление (/)","Возведение в степень (^)"]:
            return True
        else:
            return False

    def _total_validate_fields(self):
        ''' Метод общей валидации полей перейд сохранением '''        

        entry_n11 = re.match("[-+]?\d+$", self.entry_n11.get())
        entry_n12 = re.match("[-+]?\d+$", self.entry_n12.get())
        entry_n21 = re.match("[-+]?\d+$", self.entry_n21.get())
        entry_n22 = re.match("[-+]?\d+$", self.entry_n22.get())

        result_string = ''
        flag = True

        if not entry_n11:
            flag = False 
            result_string += "проверьте первый диапазон 'C'\n"
        if not entry_n12:
            flag = False 
            result_string += "проверьте первый диапазон 'ПО'\n"
        if not entry_n21:
            flag = False 
            result_string += "проверьте второй диапазон 'C'\n"
        if not entry_n22:
            flag = False 
            result_string += "проверьте второй диапазон 'C'\n"

        try:
            if int(self.entry_n12.get()) <= int(self.entry_n11.get()): 
                flag = False 
                result_string += "Второе число первого диапазона должно быль больше первого\n"
            if int(self.entry_n22.get()) <= int(self.entry_n21.get()): 
                flag = False 
                result_string += "Второе число второго диапазона должно быль больше первого\n"
        except ValueError:
            # result_string += "ValueError\n"
            flag = False

        if flag:
            self.tl_info_label.configure(text="Сохранено")
        else:
            self.tl_info_label.configure(text=result_string.rstrip("\n"))
        return flag
