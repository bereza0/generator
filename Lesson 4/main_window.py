from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox, QButtonGroup, QGroupBox


card_WIDTH, card_HIGHT = 600, 500

win_card = QWidget()
win_card.resize(card_WIDTH, card_HIGHT)
win_card.setWindowTitle('Memory Card')

btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_next = QPushButton('Відповісти')

rb_ans1 = QRadioButton("1")
rb_ans2 = QRadioButton("2")
rb_ans3 = QRadioButton("3")
rb_ans4 = QRadioButton("4")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)

lb_question = QLabel('Запитання')
lb_rest = QLabel('хвилин')
lb_result = QLabel('Правильно')
lb_right_answer = QLabel('відповідь')

sp_rest = QSpinBox()
sp_rest.setValue(30)
gb_question = QGroupBox('Варіанти відповідей')

rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)

rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)

gb_question.setLayout(rb_h1)

gb_answer = QGroupBox()

v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
gb_answer.setLayout(v1)

h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()

h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest)
h1_main.addWidget(lb_rest)

h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h3_main.addWidget(gb_answer)
h3_main.addWidget(gb_question)
gb_answer.hide()

h4_main.addStretch(1)
h4_main.addWidget(btn_next, stretch=2)
h4_main.addStretch(1)

v1_main.addLayout(h1_main, stretch=1)
v1_main.addLayout(h2_main, stretch=2)
v1_main.addLayout(h3_main, stretch=8)
v1_main.addLayout(h4_main)
v1_main.setSpacing(5)

win_card.setLayout(v1_main)


# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox, QButtonGroup, QGroupBox

# card_WIDTH, card_HIGHT = 600, 500

# win_card = QWidget()
# win_card.resize(card_WIDTH, card_HIGHT)
# win_card.setwin_cardTitle('Memory Card')
# win_card.move(300,300)

# btn_menu = QPushButton('Menu')
# btn_rest = QPushButton('Відпочити')

# sb_rest = QSpinBox()
# sb_rest.setValue(30)

# lb_rest = QLabel('Хвилини')
# lb_question = QLabel('da')

# q_rb1 = QRadioButton('da_net')
# q_rb2 = QRadioButton('da_net')
# q_rb3 = QRadioButton('da_net')
# q_rb4 = QRadioButton('da_net')

# qb_group = QButtonGroup()
# qb_group.addButton(q_rb1)
# qb_group.addButton(q_rb2)
# qb_group.addButton(q_rb3)
# qb_group.addButton(q_rb4)

# question_Group = QGroupBox('Варіанти відповей')


# line_main = QVBoxLayout()
# H_line_1 = QHBoxLayout()
# H_line_2 = QHBoxLayout()
# H_line_3 = QHBoxLayout()
# H_line_4 = QHBoxLayout()

# V_line_1 = QVBoxLayout()
# V_line_2 = QVBoxLayout()

# V_line_1.addWidget(q_rb1)
# V_line_2.addWidget(q_rb2)
# V_line_1.addWidget(q_rb3)
# V_line_2.addWidget(q_rb4)

# H_line_1.addWidget(btn_menu)
# H_line_4.addWidget(btn_rest)
# H_line_1.addWidget(sb_rest)
# H_line_1.addWidget(lb_rest)
# H_line_2.addWidget(lb_question)
# # H_line_3.addWidget(qb_group)
# H_line_3.addLayout(V_line_1)
# H_line_3.addLayout(V_line_2)

# question_Group.setLayout(H_line_3)

# line_main.addLayout(H_line_1)
# line_main.addLayout(H_line_2)
# line_main.addWidget(question_Group)
# line_main.addLayout(H_line_4)
# win_card.setLayout(line_main)