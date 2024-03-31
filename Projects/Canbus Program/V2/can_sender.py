import json
import time

from matplotlib.colors import to_hex 
from .classes.controller import Controller
from .classes.button import Button
from .classes.network import Network

NETWORK_INTERFACE = 'socketcan'
NETWORK_CHANNEL = 'vcan0'
NETWORK_BITRATE = 500000

with open("av_ctrl_msgs.json","r") as file:
    AV_MSGS = json.load(file)
AV_MODULE_ID = 0x681
AV_MODULE_REST_MSG = ['F1', '00', 'A1', '01', "FF","FF","FF","FF"]

av_net = Network(NETWORK_INTERFACE,NETWORK_CHANNEL,NETWORK_BITRATE)
av_controller = Controller(AV_MODULE_ID,AV_MODULE_REST_MSG,av_net)

def init_button():
    pass

def make_btns(controller,msg_set):
    key_set = list(msg_set.keys())[1:]
    for id in key_set:
        this_btn = Button(
            button_number=id,
            press=msg_set[id]["Press"],
            release=msg_set[id]["Release"]
        )
        try:
            this_btn.set_dial(msg_set[id]["CW"],msg_set[id]["CCW"])
        except KeyError:
            pass
        
        controller.buttons[id] = this_btn

make_btns(av_controller,AV_MSGS)

for msg in av_net.bus_agent:
    msg = hex(msg.arbitration_id)