import enum
import json
import tkinter as tk
from can_classes import MyController,MyButton,MyDial,MyNetwork
import time

#### Importing Message Data ####
# Importing the message json set.
with open("output.json","r") as file:
    json_btns = json.load(file)


#### Creating Network Controllers and Network Interface #####
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


# Creating the GUI window
root = tk.Tk()

## Creating the set of button objects based on the imported json file.
# Getting the key set, and initializing the output list.
btn_names = json_btns.keys()
btn_names = list(btn_names)

######## This list may not have any use. The thought is that objects must be saved to a variable to persist. 
input_set = []

# For each button in the list.
for i,name in enumerate(btn_names):
    
    # For each type of message for the button.
    btn_keys = json_btns[name].keys()
    
    # The [counter] clockwise message's existence are implied by the existence of the other.
    if "CCW" in btn_keys:
        
        # If the button has a counter clockwise message, create a dial object.
        this_dial = MyDial(
            controller = av_controller, 
            press_ls   = json_btns[name][ "Press"],
            cw_ls_ls   = json_btns[name][    "CW"],
            ccw_ls_ls  = json_btns[name][   "CCW"],
            release_ls = json_btns[name]["Release"],
            num=i+1,
            display=root,
        ) 
        input_set.append(this_dial)
        
    # If no rotation directions exist, the item is only a button.
    else:
        this_button = MyButton(
            press_ls= json_btns[name]["Press"],
            release_ls= json_btns[name]["Release"],
            controller= av_controller,
            num=i+1,
            display=root,
        )
        input_set.append(this_button)

# Creating the 8x8 button grid.
increment = 0
for i in range(8):
    
    for j in range(8):
        if increment == len(input_set):
            break
        else:
            if input_set[increment].__class__.__name__ == "MyDial":
                input_set[increment].canvas.grid(row=i, column=i)
            else:
                input_set[increment].config(width=25,height=25)
                input_set[increment].grid(row=i, column=j)
            
            increment+=1
    
    if increment == input_set:
        break

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
# root.after(2000, start_network)
root.mainloop()