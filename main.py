from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QColorDialog, QRadioButton, QHBoxLayout, QGroupBox
import sys


app = QApplication(sys.argv)
win = QWidget()
win.resize(400, 400)

win.setWindowTitle('Тест')

gb = QGroupBox('Варианты')
q = QLabel('Выбери цифру от 1 до 4:', alignment=Qt.AlignCenter)
rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')
btn = QPushButton('Ответить')

h_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()

v_line1.addWidget(rbtn1)
v_line1.addWidget(rbtn2)
v_line2.addWidget(rbtn3)
v_line2.addWidget(rbtn4)
h_line.addWidget(btn)

gb.setLayout(h_line)

v_line_main = QVBoxLayout()
h_line_main1 = QVBoxLayout()
h_line_main2 = QVBoxLayout()
h_line_main3 = QVBoxLayout()

h_line_main1.addWidget(q, alignment=Qt.AlignCenter)
h_line_main2.addWidget(gb)
h_line_main3.addStretch(1)
h_line_main3.addWidget(q, stretch=2)
h_line_main3.addStretch(1)

v_line_main.addLayout(h_line_main1, stretch=2)
v_line_main.addLayout(h_line_main2, stretch=8)
v_line_main.addStretch(1)
v_line_main.addLayout(h_line_main3, stretch=1)
v_line_main.addStretch(1)

win.setLayout(v_line_main)

win.show()
app.exec_()
