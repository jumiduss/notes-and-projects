from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me")
        
        self.setCentralWidget(button)


app = QApplication(sys.argv) # sys.argv gives arguments from qt6 to the display manager.
app.setApplicationName("qt_app")
# Widgets don't have parents.
# window = QWidget()

window = MainWindow()
window.show()

# Starts the event loop.
app.exec()