import time
import can

class Controller():
    
    def __init__(self):
        # super().__init__()

        # Setting up the network
        self.interface = "socketcan"
        self.channel = "vcan0"
        self.bitrate = 500000
        self.network_interface = self.setup_network()
        self.network_interface.set_filters([{"can_id":0x601, "can_mask":0x7FF}])
        self.notifier = can.Notifier(self.network_interface, [])

        # Setting up the controller's periodic message
        self.can_id = 0x681
        self.broadcast_msg = [0xF0,0x06, 0x0A, 0x01, 0xFF, 0xFF, 0xFF, 0xFF]
        self.resp_msg = [0xE0, 0xFF, 0xFF, 0xFF,  0xFF, 0xFF, 0xFF, 0xFF]
        self.broadcast_timing = 0.5
        self.periodic = self.start_periodic()

        # Declaring names for future messages.
        self.press_msg = None
        self.release_msg = None
        self.counter = 0x10
        self.got_response = True

    # Can Network, One Time Setup
    def setup_network(self):
        return can.Bus(interface=self.interface,channel=self.channel,
                        bitrate=self.bitrate)

    def start_periodic(self):
        canned_msg = self.format_can_msg(self.broadcast_msg)
        return self.network_interface.send_periodic(canned_msg,
                                                    self.broadcast_timing)

    def listener(self, can_frame: can.Message):
        msg = list(can_frame.data)
        print(msg)
        if  msg[0] == 0xE0:
            if msg[1] == self.counter:
                self.got_response = True
                self.increment_counter()
                self.format_resp_msg()
                self.notifier.remove_listener(self.listener)

    def increment_counter(self):
        if self.counter > 0x60:
            self.counter = 0x10
        else:
            self.counter += 0x10

    def format_resp_msg(self):
        self.resp_msg[1] = self.counter

    def format_can_msg(self, msg_list):
        return can.Message(arbitration_id=self.can_id, data=msg_list,
                            is_extended_id=False)

    def send_msg(self, msg):
        try:
            msg[1] = self.counter
            self.format_resp_msg()
            can_msg = self.format_can_msg(msg)
            self.got_response = False
            self.network_interface.send(can_msg)
            self.notifier.add_listener(self.listener)

        except can.CanError:
            # Program fault.
            print("Failed")

    # Message Formatting 
    def start_sending(self, press, release=None) -> None:   

        self.press_msg = press
        self.release_msg = release

        running = True
        while running:
            if self.got_response:
                if self.press_msg:
                    self.send_msg(self.press_msg)
                    
                elif self.release_msg:
                    self.send_msg(self.release_msg)
                    self.release_msg = None
                
                else:
                    break
        self.notifier.stop()
        
        
        