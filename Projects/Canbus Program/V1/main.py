import tkinter as tk
from classes.controller import MyController
from classes.button import MyButton
from classes.dial import MyDial
from classes.network import Network
import json


# Creating our base tk window for the button layout
root = tk.Tk()
root.geometry("200x1080")
root.title("AV Controller Set")
mainFrame = tk.Frame(root)

# Creating an iterable dictionary from our json set.
with open("Projects/Canbus Program/V1/testing.json","r") as file:
    json_buttons = json.load(file)


def format_list(list):
    return_list = [0xFF]*8
    for i in range(len(list)):
        return_list[i] = list[i]
    return return_list

def create_input_set(window,json_btns,controller):
    
    key_set = list(json_btns.keys())
    # Creating the row-col iterators for the tk window button-layout
    my_col = 0
    my_row = 0
    
    # Initiating return list
    input_set = []
    
    # Creating each button object
    for id in key_set:
        btn_window = window
        
        # Checking for dials
        has_dial = False
        button_keys = (json_btns[id]).keys()
        if "CW" in button_keys:
            has_dial = True
            
            # Creating dial message sets
            cw_bytes = json_btns[id]["CW"]
            ccw_bytes = json_btns[id]["CCW"]
            
            cw_msgs = []
            ccw_msgs = []
            if isinstance(cw_bytes,list):
                for i in range(4,7):
                    cw_msg = cw_bytes[:4]
                    cw_msg.append(cw_bytes[i])
                    cw_msgs.append(format_list(cw_msg))
                    
                    ccw_msg = ccw_bytes[:4]
                    ccw_msg.append(ccw_bytes[i])
                    ccw_msgs.append(format_list(ccw_msg))
            else:
                cw_msgs = cw_bytes
                ccw_msgs = cw_bytes
            # Creating dial object
            this_dial = MyDial(cw_msgs=cw_msgs,ccw_msgs=ccw_msgs,window=window,controller=controller)
            btn_window = this_dial
        # Creating the MyButton object with the messages that all networked buttons have.
        press_msg = json_btns[id]["Press"]
        release_msg = json_btns[id]["Release"]
                    
        this_btn = MyButton(
                controller=controller,
                button_number=id,
                press=press_msg,
                release=release_msg,
                root=btn_window
            )
        
        # Setting the row-col position for buttons/dials main window
        if has_dial:
            # Adding the dial's button to the dial object
            this_dial.add_btn(this_btn)
            # # Setting the dial groups position
            this_dial.grid(row=my_row,column=my_col)
            this_object = this_dial
        else:
            this_btn.grid(row=my_row,column=my_col)
            this_object= this_btn
            
        # Incrementing the row-col position for the next button object
        if my_col > 3:
            my_col = 0
            my_row += 1
        else:
            my_col += 1
        
        # this_object.pack()
        # Adding the buttons to a list to be returned at the end of the function 
        input_set.append(this_object)

    return input_set

av_network = Network("socketcan","vcan0",500000)
av_controller = MyController(0x681,[0xF0, 0x06, 0x0A, 0x01, 0xFF, 0xFF,0xFF,0xFF])
av_buttons = create_input_set(root,json_buttons,av_controller)

running = True
# Starting network and messages 
with av_network.bus_agent as bus:
    av_controller.add_net_con(av_network)
    av_controller.start_periodic()                
    root.mainloop()