from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(220, 225, 500, 600)
		self.setWindowTitle("Hello")

		self.initUI()

	def initUI(self):
		self.lbl = QtWidgets.QLabel(self)
		self.lbl.setText("Hallo!")
		self.lbl.move(20,50)
		
		self.btn = QtWidgets.QPushButton(self)
		self.btn.setText("Hallo!")
		self.btn.move(400, 550)
		self.btn.clicked.connect(self.clicked)

	def clicked(self):
		self.lbl.setText("I've clicked! sadsadsdsdsdsadsadsadsadsadsadsad")
		self.update()

	def update(self):
		self.lbl.adjustSize()

def window():
	app = QApplication(sys.argv)
	win = MyWindow()

	win.show()
	sys.exit(app.exec_())

window()
