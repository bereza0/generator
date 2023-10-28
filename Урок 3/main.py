from random import randint as rnd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

def show_win():
    message = QMessageBox()
    message.setText('Правильно! Ви виграли гіроскутер')
    message.exec_()

def show_da():
    message = QMessageBox()
    message.setText('Ні, в 2015 році. Ви виграли фірмовий плакат')
    message.exec_()

WIDTH = 400
HEIGNT = 200

app = QApplication([])
mw = QWidget()
mw.resize(WIDTH, HEIGNT)
mw.setWindowTitle('Конкурс від Crazy People')


question = QLabel('В якому році канал отримав" золоту кнопку "від YouTube?')

btn1 = QRadioButton('2005')
btn2 = QRadioButton('2010')
btn3 = QRadioButton('2015')
btn4 = QRadioButton('2020')

l_main = QVBoxLayout()
lH1 = QHBoxLayout()
lH2 = QHBoxLayout()
lH3 = QHBoxLayout()

lH1.addWidget(question, alignment=Qt.AlignCenter)
lH2.addWidget(btn1, alignment=Qt.AlignCenter)
lH2.addWidget(btn2, alignment=Qt.AlignCenter)
lH3.addWidget(btn3, alignment=Qt.AlignCenter)
lH3.addWidget(btn4, alignment=Qt.AlignCenter)

l_main.addLayout(lH1)
l_main.addLayout(lH2)
l_main.addLayout(lH3)


btn1.clicked.connect(show_da)
btn2.clicked.connect(show_da)
btn3.clicked.connect(show_win)
btn4.clicked.connect(show_da)

mw.setLayout(l_main)
mw.show()
app.exec_()