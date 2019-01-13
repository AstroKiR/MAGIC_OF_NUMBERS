#!/usr/bin/env python3

import configparser
import random
import re

from tkinter import Tk, PhotoImage, Menu
from tkinter.ttk import *

from classes import MAIN_WINDOW, PREFERENCE_WINDOW, CUSTOM_STYLE


class TkMathTrickTrainer(Tk):
    """ Класс обертка 
        самого приложения
    """     
    def __init__(self, *args, **kwargs):
        ''' Конструктор '''
        Tk.__init__(self, *args, **kwargs)
        self.preference_window = None
        imgicon = PhotoImage(file="calc.png")
        self.tk.call('wm', 'iconphoto', self._w, imgicon)
        self.style = CUSTOM_STYLE()
        self._main_menu()
        self.main_window = MAIN_WINDOW(self)
        self.main_window.pack(expand="100", fill="both")

    def _show_preference_window(self):
        ''' Метод отображает единственное окно настроек,
            если окно свернуто, оно разворачивается и на нем устанавливается фокус
        '''
        if self.preference_window is None or not self.preference_window.winfo_exists():
            self.preference_window = PREFERENCE_WINDOW()
        else:
            if self.preference_window.state() == "iconic":
                self.preference_window.state(newstate="normal")
            self.preference_window.lift()
            self.preference_window.focus_force()
            self.preference_window.grab_set()
            self.preference_window.grab_release()

    def _main_menu(self):
        ''' Метод формирует верхнее меню приложения '''
        main_menu = Menu(bd=0, activebackground="#93CEE9")
        self.configure(menu=main_menu)
        main_menu.add_command(label="Настройка", font=("Arial", 10), command=lambda: self._show_preference_window())
        # main_menu.add_command(label="Справка", font=("Arial", 10), command=self.quit)
        

if __name__ == "__main__":
    root = TkMathTrickTrainer()
    root.title("Счет в уме")
    # root.minsize(600, 180)
    root.mainloop()

