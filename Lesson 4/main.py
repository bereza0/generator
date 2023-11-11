from random import choices as chc
from random import shuffle as shf
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

app = QApplication([])

from main_window import *





class Question():
    def __init__(self, text, versions):
        self.question = text
        self.right_answer = versions[0]
        self.ans_2 = versions[1]
        self.ans_3 = versions[2]
        self.ans_4 = versions[3]
        self.attempts = 0
        self.success = 0

    def return_text(self):
        return self.question

    def got_right(self):
        self.attempts += 1
        self.success += 1

    def got_wrong(self):
        self.attempts += 1


question_1 = Question('Яблуко', ['apple', 'aplication', 'pineapple', 'apply'])
question_2 = Question('Дім', ['house', 'horse', 'hurry', 'hour'])
question_3 = Question('Миша', ['mouse', 'mouth', 'mose', 'museum'])
question_4 = Question('Число', ['number', 'digit', 'amount', 'summery'])

radio_list = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
question_list = [question_1 ,question_2, question_3, question_4]

def new_question():
    global current_question
    current_question = chc(question_list)
    lb_question.setText(current_question.text)
    lb_right_answer.setText(current_question.right_answer)
    shf(radio_list)
    radio_list[0].setText(current_question.right_answer)
    radio_list[1].setText(current_question.ans_2)
    radio_list[2].setText(current_question.ans_3)
    radio_list[3].setText(current_question.ans_4)

new_question()

win_card.show()
app.exec_()