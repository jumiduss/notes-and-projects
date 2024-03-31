import can
import tkinter as tk
import threading
from pyparsing import col

###### Looking for the return message of [0xE0. Clock_of_Last_Send, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

class MyGui(threading.Thread):
    def __init__(self):
        self.root = tk.Tk()




class MyNetwork():
    def __init__(self, interface, channel, bitrate):
        can.rc['interface'] = interface
        can.rc['channel']= channel
        can.rc['bitrate']= bitrate
        self.bus_agent = can.Bus()
        self.channel = channel




class MyButton(tk.Button):
    def __init__(self, press_ls, release_ls, controller, num, display, dial=False):
        
        # Setting the press and release codes for this btn.
        self.press = press_ls
        self.release = release_ls
        
        # Adding a controller reference to edit the on_press/on_release messages.
        self.controller = controller
        
        # Setting up the gui button
        tk.Button.__init__(self,display,text=num)
        if not dial:
            self.config(width=15,height=15)

    def on_release(self):
        '''Removes the option of using the pressed message from the controller, which triggers the controller's next_msg to send the release message.'''
        self.controller.btn_pressed = None
        
    def on_press(self):
        self.controller.btn_pressed = self.press
        self.controller.btn_released = self.release




class MyDial():
    
    def __init__(self, ccw_ls_ls, cw_ls_ls, press_ls, release_ls, controller, num, display):
        
        # Setting the Clockwise, and Counter Clockwise message sets.
        self.ccw = ccw_ls_ls
        self.cw = cw_ls_ls
        self.controller = controller
        
        #### Setting up GUI ####
        
        # Canvas
        self.canvas = tk.Canvas(display)
        self.config()
        
        # Creating the dial's center button.
        self.center_btn = MyButton(press_ls, release_ls, controller, num, self.canvas)
        
        # Configuring the center button on the canvas.
        self.center_btn.config(height=15,width=5)
        self.center_btn.grid(row=0,column=1)
        
        # Creating the dial direction sliders.
        self.dial_1 = self.create_dial("ccw")
        self.dial_2 = self.create_dial("cw")
        
    def create_dial(self, name):
        dial = tk.Scale(self.canvas, from_=0, to=3, name=name, orient=tk.VERTICAL, command=self.on_cw)
        dial.bind("<ButtonRelease>", self.dial_stop)
        dial.config(width=5)
        
        if name == "cw":
            dial.grid(row=0, column=2)
        else:
            dial.grid(row=0, column=0)
            
        return dial
    
    def dial_stop(self, event):
        self.dial_1.set(0)
        self.dial_2.set(0)
        
#######################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #### Can possibly simplify these into one method #####
    def on_cw(self, event):        
        
        event = int(event) # whatever the event slider value is, between 0 and 3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        # If the dial isn't moving, reset the message on the controller.
        if event == 0:
            self.controller.btn_pressed = None
        else:
            self.controller.btn_pressed = self.cw[event - 1]

    def on_ccw(self,event):        
        event = int(event) # whatever the event slider value is, between 0 and 3
        
        # If the dial isn't moving, reset the message on the controller.
        if event == 0:
            self.controller.btn_pressed = None
        else:
            self.controller.btn_pressed = self.ccw[event - 1]




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