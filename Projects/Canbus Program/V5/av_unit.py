import can
import json
import sys
import os

class Controller():
    
    def __init__(self):
        super().__init__()
        
        # Setting up the network
        self.interface = "socketcan"
        self.channel = "vcan0"
        self.bitrate = 500000
        self.network_interface = self.setup_network()
        self.network_interface.set_filters([{"can_id":0x681, "can_mask":0x7FF}])
        
        # Setting up the controller's periodic message
        self.can_id = 0x601
        self.broadcast_msg = [0xF1,0x00, 0x0A, 0x01, 0xFF, 0xFF, 0xFF, 0xFF]
        self.broadcast_timing = 0.5
        self.periodic = self.start_periodic()
        self.msg_set = self.create_msgs()
        self.notifier = can.Notifier(self.network_interface, [self.listener])

    # Can Network, One Time Setup
    def setup_network(self):
        return can.Bus(interface=self.interface,channel=self.channel,
                        bitrate=self.bitrate)
        
    def start_periodic(self):
        canned_msg = can.Message(arbitration_id=self.can_id, data=self.broadcast_msg, is_extended_id=False)
        return self.network_interface.send_periodic(canned_msg, self.broadcast_timing)

    def create_msgs(self):
        with open("/home/jd/Documents/CodingProjects/Canbus Program/After Studying Dead Simple Python/Pre Stack Exchange/output.json", "r") as file:
            msg_dict = json.load(file)
        
        msgs = []

        for key, dict_msg_types in msg_dict.items():
            for msg_type, dict_msgs in dict_msg_types.items():
                if isinstance(dict_msgs, dict):
                    for speed, msg in dict_msgs.items():
                        msgs.append(msg)
                else:
                    if isinstance(dict_msgs, list):
                        msgs.append(dict_msgs)
        
        return msgs
    
    def listener(self, msg: can.Message):
        msg_data = list(msg.data)
        if msg_data[0] != 0xF0:
            counter = msg_data[1]
            msg_data[1] = 0xFF
            
            if msg_data in controller.msg_set:
                return_list = [0xE0, counter, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                return_msg = can.Message(arbitration_id=0x601, data=return_list, is_extended_id=False)
                self.network_interface.send(return_msg)


if __name__ == "__main__":
    try:
        controller = Controller()
        with controller.network_interface as bus:
            for msg in bus:
                continue
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
