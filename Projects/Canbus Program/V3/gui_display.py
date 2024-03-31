from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QGridLayout

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.ad

app = QApplication(sys.argv)
app.setApplicationName("qt_app")

window = MainWindow()
window.show()

app.exec()