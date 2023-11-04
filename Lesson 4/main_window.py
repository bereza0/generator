from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox, QButtonGroup, QGroupBox

card_WIDTH, card_HIGHT = 600, 500

win_card = QWidget()
win_card.resize(card_WIDTH, card_HIGHT)
win_card.setWindowTitle('Memory Card')
win_card.move(300,300)

btn_menu = QPushButton('Menu')
btn_rest = QPushButton('Відпочити')

sb_rest = QSpinBox()
sb_rest.setValue(30)

lb_rest = QLabel('Хвилини')
lb_question = QLabel('da')

q_rb1 = QRadioButton('da_net')
q_rb2 = QRadioButton('da_net')
q_rb3 = QRadioButton('da_net')
q_rb4 = QRadioButton('da_net')

qb_group = QButtonGroup()
qb_group.addButton(q_rb1)
qb_group.addButton(q_rb2)
qb_group.addButton(q_rb3)
qb_group.addButton(q_rb4)

question_Group = QGroupBox('Варіанти відповей')


line_main = QVBoxLayout()
H_line_1 = QHBoxLayout()
H_line_2 = QHBoxLayout()
H_line_3 = QHBoxLayout()

V_line_1 = QVBoxLayout()
V_line_2 = QVBoxLayout()

V_line_1.addWidget(q_rb1)
V_line_2.addWidget(q_rb2)
V_line_1.addWidget(q_rb3)
V_line_2.addWidget(q_rb4)

H_line_1.addWidget(btn_menu)
H_line_1.addWidget(btn_rest)
H_line_1.addWidget(sb_rest)
H_line_1.addWidget(lb_rest)
H_line_2.addWidget(lb_question)
# H_line_3.addWidget(qb_group)
H_line_3.addLayout(V_line_1)
H_line_3.addLayout(V_line_2)

question_Group.setLayout(H_line_3)

line_main.addLayout(H_line_1)
line_main.addLayout(H_line_2)
line_main.addWidget(question_Group)
win_card.setLayout(line_main)