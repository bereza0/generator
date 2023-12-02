from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox
from ui import Ui_MainWindow

class Widget(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.btn_ganerate.clicked.connect(self.example)

    def generate(self):
        self.label_password.setText('da')
        print(1)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()