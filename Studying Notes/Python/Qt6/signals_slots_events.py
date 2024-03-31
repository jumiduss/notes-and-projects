import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Part 3
        self.button_is_checked = True
        
        # Default
        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        
        ## Parts 1 and 2
        # button.clicked.connect(self.the_button_was_clicked)
        
        # Parts 2 and 3
        button.clicked.connect(self.the_button_was_toggled)
        # Part 4
        button.setChecked(self.button_is_checked)
        
        self.setCentralWidget(button)
        
        
        
    def the_button_was_clicked(self):
        print("Clicked!")
        
    def the_button_was_toggled(self, checked):
        
        print("Checked?", checked)
        
        
app = QApplication(sys.argv)
app.setApplicationName("qt_app")

window = MainWindow()
window.show()

app.exec()