import PyQt6.QtWidgets as qw
from PyQt6.QtCore import Qt
import asyncio

import sys
import json

from controller import Controller

def import_dict():
    with open("Projects/Canbus Program/V5/output.json", "r") as file:
        return json.load(file)

class MyButton(qw.QPushButton):
    def __init__(self, id, data):
        super().__init__(id)
        self.id = id
        self.data = data
        self.press_msg = self.data["Press"]
        self.release_msg = self.data["Release"]

class MyDial(qw.QSlider):
    def __init__(self, id, data):
        super().__init__()
        self.id = id
        self.data = data
        if isinstance(data, dict):
            self.speed = (data['0'], data['1'], data['2'])       
        else:
            self.speed = data
        
        self.setRange(0,3)
        self.setMaximumHeight(90)

class DialGroup(qw.QWidget):
    def __init__(self, group_id, data):
        super().__init__()
        self.setGeometry(0, 0, 100, 100)
        
        # Creating Grid Layout 
        hor_layout = qw.QGridLayout()
        
        # Creating Grid Objects
        self.ccw = MyDial(group_id, data["CCW"])
        self.ccw_label = qw.QLabel("0", self)
        self.btn = MyButton(group_id, data)
        self.cw = MyDial(group_id, data["CW"])
        self.cw_label = qw.QLabel("0", self)
        
        # Grid Object Configuration
        self.ccw_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cw_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.ccw.sliderReleased.connect((self.ccw_slider_release))
        self.cw.sliderReleased.connect((self.cw_slider_release))        
        
        hor_layout.addWidget(self.ccw_label, 0, 0, 
                            Qt.AlignmentFlag.AlignBottom)
        hor_layout.addWidget(self.cw_label, 0, 2, 
                            Qt.AlignmentFlag.AlignBottom)
        hor_layout.addWidget(self.ccw, 1, 0, 
                            Qt.AlignmentFlag.AlignTop)
        hor_layout.addWidget(self.btn, 0, 1, 2, 1, 
                            Qt.AlignmentFlag.AlignCenter)
        hor_layout.addWidget(self.cw, 1, 2, 
                            Qt.AlignmentFlag.AlignTop)
        
        self.setLayout(hor_layout)

        
    def cw_slider_release(self):
        self.cw.setSliderPosition(0)
        print("Slider Off")
        
    def ccw_slider_release(self):
        self.ccw.setSliderPosition(0)
        print("Slider Off")

class Window(qw.QWidget):
    
    def __init__(self, data, cntrlr):
        super().__init__()
        self.setWindowTitle("Button Set")
        self.setGeometry(0, 0, 1000, 1000)
        
        self.grid = qw.QGridLayout()
        self.grid_items = self.create_items(data)
        self.add_grid_items(self.grid_items)
        self.setLayout(self.grid)
        
        self.controller = cntrlr
                
        for in_item in self.grid_items:
            if type(in_item) is DialGroup:
                self.set_dial_commands(in_item)
                
            elif type(in_item) is MyButton:
                self.set_btn_commands(in_item)

    # Setting up the Window
    def create_items(self, data_list):
        out_list = []
        for btn_id, sig_types in data_list.items():
            if len(sig_types) > 2:
                item = DialGroup(group_id=btn_id, data=sig_types)
            else:
                item = MyButton(id=btn_id, data=sig_types)
            out_list.append(item)
        return out_list

    def add_grid_items(self, item_list):
        # Grid Size is 7 x 7
        i = j = 0
        
        def k(m):
            return 0 if m > 5 else m+1
        
        for item in item_list:
            self.grid.addWidget(item, i, j)
            j = k(j)
            if j == 0:
                i+=1

    def dial_speeds(self, dial, label):
        
        value = dial.value()  
        label.setText(str(value))
        slice_index = int(value) - 1
        speeds = dial.speed
        
        if int(value) > 0:
            if isinstance(speeds, tuple):
                spec_speed = speeds[slice_index]
                self.controller.set_msgs(press=spec_speed)
                self.controller.send_press()
            else:
                print("Non-Can Message: " + speeds)

    def set_btn_commands(self, btn):
        btn.pressed.connect(lambda: self.btn_press(btn))
        btn.released.connect(lambda: self.btn_release())

    def set_dial_commands(self, group_obj):
        # Possible conflict with mutable cw ccw objects sending the same message across the board.
        # Although, it may be saved top the class instance.
        
        self.set_btn_commands(group_obj.btn)
        
        cw = group_obj.cw
        cw_label = group_obj.cw_label
        cw.valueChanged.connect(lambda:self.dial_speeds(dial=cw, label=cw_label))
        
        ccw = group_obj.ccw
        ccw_label = group_obj.ccw_label
        ccw.valueChanged.connect(lambda:self.dial_speeds(dial=ccw, label=ccw_label))


    # Button Interactions
    def btn_press(self, obj_inst):
        print("Press")
        if isinstance(obj_inst.press_msg, list):
            asyncio.run(
                self.controller.start_sending(
                    press = obj_inst.press_msg, 
                    release = obj_inst.release_msg))
            
        else:
            print(obj_inst.press_msg)

    def btn_release(self):
        print("Release")
        self.controller.press_msg = None



# Main Loop
def create_window(window = None):
    app = qw.QApplication(sys.argv)
    app.setApplicationName("qt_app")
    
    data = import_dict()
    controller = Controller()
    window = Window(data, controller)
    window.show()
    sys.exit(app.exec())
    

if __name__ =="__main__":
    create_window()