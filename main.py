from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QLabel, QVBoxLayout, QColorDialog, QRadioButton, QHBoxLayout, QGroupBox
import sys


app = QApplication(sys.argv)
win = QWidget()
win.resize(400, 400)

win.setWindowTitle('Тест')

gb = QGroupBox('Варианты')

gb_result = QGroupBox('Результат теста')
lbl_r_a = QLabel('Правильный ответ 3')
v_line_result = QVBoxLayout()

v_line_result.addWidget(lbl_r_a, alignment=Qt.AlignCenter)
gb_result.setLayout(v_line_result)

q = QLabel('Выбери цифру от 1 до 4:', alignment=Qt.AlignCenter)
rg = QButtonGroup()

rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')
btn = QPushButton('Ответить')

rg.addButton(rbtn1)
rg.addButton(rbtn2)
rg.addButton(rbtn3)
rg.addButton(rbtn4)

def show_question():
    gb.show()
    gb_result.hide()
    btn.setText('Ответить')
    btn.clicked.connect(show_result)
    rg.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    rg.setExclusive(True)

def show_result():
    gb.hide()
    gb_result.show()
    btn.setText('Следующий вопрос')
    btn.clicked.connect(show_question)

btn.clicked.connect(show_result)

h_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()

v_line1.addWidget(rbtn1)
v_line1.addWidget(rbtn2)
v_line2.addWidget(rbtn3)
v_line2.addWidget(rbtn4)
h_line.addLayout(v_line1)
h_line.addLayout(v_line2)

gb.setLayout(h_line)

v_line_main = QVBoxLayout()
h_line_main1 = QVBoxLayout()
h_line_main2 = QVBoxLayout()
h_line_main3 = QVBoxLayout()

h_line_main1.addWidget(q, alignment=Qt.AlignCenter)
h_line_main2.addWidget(gb)
h_line_main2.addWidget(gb_result)
h_line_main3.addStretch(1)
h_line_main3.addWidget(btn, stretch=2)
h_line_main3.addStretch(1)

v_line_main.addLayout(h_line_main1, stretch=2)
v_line_main.addLayout(h_line_main2, stretch=8)
v_line_main.addStretch(1)
v_line_main.addLayout(h_line_main3, stretch=1)
v_line_main.addStretch(1)

gb_result.hide()

win.setLayout(v_line_main)

win.show()
app.exec_()
