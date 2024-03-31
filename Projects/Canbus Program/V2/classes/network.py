import can

class Network:
    
    def __init__(self, interface, channel, bitrate):
        can.rc['interface'] = interface
        can.rc['channel']= channel
        can.rc['bitrate']= bitrate
        self.bus_agent = can.Bus()
        self.channel = channel
                
    def send_msg(self,can_msg):
        try:
            self.bus_agent.send(can_msg)
            print(f"Message send on {self.channel}")
        except can.CanError:
            print("Message NOT sent")