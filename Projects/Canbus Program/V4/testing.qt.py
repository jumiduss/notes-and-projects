import sys
import can
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, group

###### Looking for the return message of [0xE0. Clock_of_Last_Send, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]


# Creating the main widget on the window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.layout = QGridLayout()

        self.json_dict = self.grab_file()
        self.container = QWidget()
        self.button_list = []
        self.make_buttons()
        self.setup_button_commands()
        
        self.container.setLayout(self.layout)
        
        self.setCentralWidget(self.container)


    ####################################################
    ############## Importing the JSON Set ##############

    def grab_file(self):
        '''Importing the message json set.'''
        
        with open("qt6/qt_output.json","r") as file:
            return json.load(file)


    ####################################################
    ############## Creating Input Objects ##############

    def make_buttons(self):
        
        for i, value in enumerate(self.json_dict.values()):
            print(value["Press"])
            
            this_button = QPushButton(str(i + 1), self.container)
            this_button.pressed(self.on_press(value["Press"]))
            
    ## Old Button Creation
    # def make_buttons(self):
    #     '''Adds the controller inputs to a grid set'''
        
    #     # Getting the key set, and initializing the output list.
    #     btn_names = self.json_dict.keys()
    #     btn_names = list(btn_names)

    #     # For each button in the list.
    #     for i,name in enumerate(btn_names):
            
    #         # For each type of message for the button.
    #         btn_keys = self.json_dict[name].keys()
            
    #         # # If the button has a counter clockwise message, create a dial object.
    #         # # The existence of either clockwise/counter-clockwise message's imply both exist, and the button is a dial group.
    #         # if "CCW" in btn_keys:
                
    #         #     this_dial = MyDial(
    #         #         press_ls   = self.json_dict[name][  "Press"],
    #         #         cw_ls_ls   = self.json_dict[name][     "CW"],
    #         #         ccw_ls_ls  = self.json_dict[name][    "CCW"],
    #         #         release_ls = self.json_dict[name]["Release"],
    #         #         btn_num    =                             i+1,
    #         #         parent     =                  self.container,
    #         #     )
    #         #     self.add_grid_cell(this_dial, i)
                
    #         # If no rotation directions exist, the item is only a button.
    #         # else:
    #         this_button = MyButton(
    #             release_ls = self.json_dict[name]["Release"],
    #             press_ls   = self.json_dict[name][  "Press"],
    #             parent     = self.container,
    #             btn_name   = i + 1,
    #             width      = 25,
    #             height     = 25,
    #         )
    #         self.button_list.append(this_button)
    #         self.add_grid_cell(this_button, i)

    def add_grid_cell(self,input_obj, index):
        '''Adds a widget to the grid layout.'''

        column_quantity = 7
        row_quantity    = 7

        row = int(index / row_quantity)
        column = (column_quantity - (index % column_quantity))

        self.layout.addWidget(input_obj,row,column)

    def setup_button_commands(self):
        for input_obj in self.button_list:
            # if input_obj.dial:
            #     input_obj.button
            input_obj.pressed.connect(lambda: self.on_press(input_obj.name - 1))

    def on_press(self,msg):
                print()


class MyButton(QPushButton):
    def __init__(self, press_ls, release_ls, btn_name, parent, width, height, dial = False):
        
        # Identifier for buttons within a dial group
        self.dial = dial
        # Creating the gui element
        super().__init__(parent=parent)
        self.setFixedSize(width, height)
        self.clicked.connect(self.on_click)
        
        # Setting the press and release codes for this btn.
        self.press = press_ls
        self.release = release_ls
        
        # Setting the button's gui text.
        self.name = btn_name
        
    def on_click(self):
        print("Clicked")

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("qt_app")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
    



