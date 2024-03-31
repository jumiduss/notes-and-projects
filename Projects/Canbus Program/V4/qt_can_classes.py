import can
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QVBoxLayout, QWidget
###### Looking for the return message of [0xE0. Clock_of_Last_Send, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        



class MyNetwork():
    def __init__(self, interface, channel, bitrate):
        can.rc['interface'] = interface
        can.rc['channel']= channel
        can.rc['bitrate']= bitrate
        self.bus_agent = can.Bus()
        self.channel = channel

class MyController(MyNetwork):
    
    #### Controller Initialization ####
    ###################################
    def __init__(self, can_id, rest_msg, network):
        
        # Each controller has a shared network that it's attached to.
        self.network = network
        
        # Each controller has a unique ID, and broadcast message on the network.
        self.id = can_id
        self.rest_msg = self.format_con_msg(rest_msg)
                
        # Setting the initial message loop-counter.
        self.msg_clock = 0x00
        
        # Specifying the expected format of an acknowledge message.
        self.expected_response = [0xE0,self.msg_clock,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Initiating the message variables that the buttons update on press / release.
        self.btn_pressed = None
        self.btn_released = None


    #### Controller Periodic Message Methods ####
    #############################################
    def start_periodic(self):
        '''Starts the periodic send method for the controller.'''
        # Setting the periodic message as a task variable.
        self.con_periodic = self.network.bus_agent.send_periodic(self.rest_msg, 0.50)
        assert isinstance(self.con_periodic, can.CyclicSendTaskABC)
        
    def stop_periodic(self):
        '''Stops the periodic send method for the controller.'''
        self.con_periodic.stop()


    #### Message Configuration Methods ####
    #######################################
    def set_messages(self, press, release):
        '''Sets the on_press and on_release actions of the buttons and dials.'''
        
        # Dials set the on_release message to None since they only trigger by clicks per 1000 microseconds.
        self.btn_pressed = press
        self.btn_released = release
        

    def set_msg_clk_byte(self, msg):
        '''Takes any non-broadcast controller message and replaces the clock byte.'''
        
        msg[1] = self.step_msg_clock()
        return msg
    
    
    def format_con_msg(self, msg_l):
        '''Takes a can message and returns a CAN message-frame as an object.'''
        
        return can.Message(
            arbitration_id=self.id,
            data=msg_l,
            is_extended_id=False,
        )
        
        
        
    #### Message Transmission Methods ####
    ######################################
    def step_msg_clock(self):
        '''Increments the controller's "message loop-counter," and updates the controller counter variable.'''
        
        # The max value of the message loop-counter is 0x70, which resets to 0x10.
        if self.msg_clock > 0x60:
            self.msg_clock = 0x00
            
        # Increment by 0x10 regardless.
        self.msg_clock += 0x10
        
        # Updating the acknowledge message's "message loop-counter" byte.
        self.expected_response[1] = self.msg_clock
        
        
    def btn_release(self):
        
        # If a release message exists, send it.
        if self.btn_released:
            self.try_send(self.btn_released)
            
        # Clear the on_press and on_release messages.
        self.btn_pressed = None
        self.btn_released = None


    def try_send(self, msg):
        self.on_deck_msg = self.format_msg(msg)
        try:
            self.network.bus_agent.send(self)
            print(f"Message sent successfully on {self.channel}")
        except can.CanError:
            print("Error, Message NOT sent")


    def next_msg(self):
        if self.btn_pressed:
            self.try_send(self.btn_pressed)
        elif self.btn_released:
            self.try_send(self.btn_released)