from queue import Queue
import can
from PySide6.QtWidgets import (QLabel, QPushButton, QWidget,
                                QMainWindow, QVBoxLayout, QApplication)
from PySide6.QtCore import QThread

queue = Queue()

class Controller(QThread):
    
    def __init__(self):
        super(Controller, self).__init__(
            
        )
        

    def run(self):
        mode = "none"
        while True:
            _mode = queue.get()
            
            if mode != _mode:
                mode = _mode
                print(f"mode: {mode}")
            
            if mode == "Stop":
                break
            
            if mode == "Start":
                self.run_network()
    
    def run_network(self):
        bus = can.Bus(channel="vcan0", interface="socketcan")
        with bus:
            for msg in bus:
                print(msg)
                if queue == "Stop":
                    break



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        label = QLabel("Network Controller")
        btn1 = QPushButton("Start Network")
        btn2 = QPushButton("Stop Network")
        layout.addWidget(label)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        btn1.clicked.connect(self.mode1)
        btn2.clicked.connect(self.mode2)
        self.show()

        self.worker = Controller()  # Create a Worker instance
        self.worker.start()  # Start the Worker instance (which calls the run function of the Worker instance)

    def mode1(self):
        queue.put("Start")

    def mode2(self):
        queue.put("Stop")

    def closeEvent(self, event):
        self.worker.terminate()  # When the window closes, stop the thread

if __name__ == '__main__':

    app = QApplication()
    app.setApplicationName("qt_apps")
    window = MainWindow()
    app.exec()
