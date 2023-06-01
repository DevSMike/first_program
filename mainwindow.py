from tkinter import *
from creational.singleton import Singleton
import eqswindow

class Window(Tk, Singleton):
    def init(self):
        print('calling from init')
        super().__init__()

        self.button = Button(self, text='open an eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswindow.Extra()

    def __init__(self):
        print('calling from init')