import json
from qt_can_classes import MyController,MyButton,MyDial,MyNetwork
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QMainWindow
import sys
import time


####################################################
############## Creating Network Controllers and Network Interfaces ##############
# Initializing the connection interface.
sub_network = MyNetwork("socketcan","vcan0",500000)

# Initializing the controller we are trying to mimic in software.
av_controller = MyController(
    0x681,
    [
        0xF0,0x06, 0x0A, 0x01, 0xFF, 0xFF, 0xFF, 0xFF
    ],
    sub_network,
)

# Initializing the AV Radio to check when to start broadcast messages on av_controller.
av_receiver = MyController(
    0x601,
    [0xF1, 0x00, 0x0A,0xFF,0xFF,0xFF,0xFF,0xFF],
    sub_network,
)

##### #Canbus Stuff # #####
# Setting a one off start periodic after a certain time interval from the AV Unit
not_set = True
def start_network():
    with sub_network.bus_agent as bus:
        now = time.time()
            
        for msg in bus:
            print(msg)
            new_msg = list(msg.data)
            
            # Starting the broadcast message for the AV Controller.
            if not_set and msg.data == av_receiver.rest_msg:
                if (time.time() - now) > 0.425:
                    av_controller.start_periodic()
                    
            # Checking for acknowledgement responses.
            if new_msg[0] == 0xE0:
                print(new_msg)
                if new_msg[1] == av_controller.msg_clock:
                    av_controller.next_msg()
                else:
                    print("Error in AV Controller's Response Message")
    av_controller.stop_periodic()





