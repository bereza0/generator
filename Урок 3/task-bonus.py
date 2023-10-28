from random import randint as rnd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

def show_win():
    message = QMessageBox()
    message.setText('Ви виграли зустріч з творцями каналу!')
    message.exec_()

def show_da():
    message = QMessageBox()
    message.setText('Пощастить іншим разом!')
    message.exec_()

WIDTH = 400
HEIGNT = 200

app = QApplication([])
mw = QWidget()
mw.resize(WIDTH, HEIGNT)
mw.setWindowTitle('Конкурс від Crazy People')


question = QLabel('Як звали першого ютуб-блогера, який набрав 100 млн. підписників?')

btn1 = QRadioButton('PewDiePie')
btn2 = QRadioButton('Рет і Лінк')
btn3 = QRadioButton('SlivkiShow')
btn4 = QRadioButton('TheBrianMaps')
btn5 = QRadioButton('Mister Max')
btn6 = QRadioButton('EeOneGuy')

l_main = QVBoxLayout()
lH1 = QHBoxLayout()
lH2 = QHBoxLayout()
lH3 = QHBoxLayout()
lH4 = QHBoxLayout()

lH1.addWidget(question, alignment=Qt.AlignCenter)
lH2.addWidget(btn1, alignment=Qt.AlignCenter)
lH2.addWidget(btn2, alignment=Qt.AlignCenter)
lH3.addWidget(btn3, alignment=Qt.AlignCenter)
lH3.addWidget(btn4, alignment=Qt.AlignCenter)
lH4.addWidget(btn5, alignment=Qt.AlignCenter)
lH4.addWidget(btn6, alignment=Qt.AlignCenter)

l_main.addLayout(lH1)
l_main.addLayout(lH2)
l_main.addLayout(lH3)
l_main.addLayout(lH4)


btn1.clicked.connect(show_win)
btn2.clicked.connect(show_da)
btn3.clicked.connect(show_da)
btn4.clicked.connect(show_da)
btn5.clicked.connect(show_da)
btn6.clicked.connect(show_da)

mw.setLayout(l_main)
mw.show()
app.exec_()