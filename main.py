from random import randint as rnd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, Qwidget


WIDTH = 500
HEIGNT = 500

app = QApplication([])


class Button():
    def __init__(self, width, height, x, y, text, color):
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.bool = True
    
    # def change_text(self, text):


    def show(self):
        self.bool = True

    def hide(self):
        self.bool = False

    def print_info(self):
        print(f'{self.text} {self.x} {self.y} {self.bool}')


number = rnd(1, 100)


button = Button(1, 1, 100, 100, 'ok', 'Grey' )

button.hide()
button.print_info()
button.show()
button.print_info()