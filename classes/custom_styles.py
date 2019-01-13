from tkinter.ttk import *


class CUSTOM_STYLE(Style):

    def __init__(self, *args, **kwargs):
        Style.__init__(self, *args, **kwargs)
        self.theme_use("clam")
        self._custom_frame()
        self._custom_buttom()


    def _custom_frame(self):
        self.configure("TFrame",
            background="#EFF0F1"
        )


    def _custom_buttom(self):
        self.configure("TButton", 
            background="#C8CACC",
            foreground="#000000",
            relief="FLAT"
        )
        self.map("TButton",
            foreground=[("pressed", "#1e1e1e"), ("active", "#000")],
            background=[("disabled", "#99c0ff"), ("pressed", "!disabled", "#93CEE9"), ("active", "#93CEE9")]
        )
