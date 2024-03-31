import can
class MyController:

    def __init__(self,id,rest_msg):
        self.id = id
        self.rest = rest_msg
        self.network = None
        self.task = None
        self.button_pressed = None
        self.counter = 0x0

    def incr_count(self):
        if self.counter == 0x70:
            self.counter = 0x10
        else:
            self.counter += 0x10
        
    def add_net_con(self, network):
        self.network = network

    def get_btn_msg(self,msg):
        self.incr_count()
        msg[1] = self.counter
        
        return can.Message(
            # This arbitration id is the ID of the controller.
            arbitration_id = self.id,
            data = msg,
            is_extended_id = False
        )
    
    def get_con_msg(self):
        return can.Message(
            arbitration_id=self.id,
            data = self.rest,
            is_extended_id=False
        )
        
    def send_msg(self,input_msg):
        this_msg = self.get_btn_msg(input_msg)
        self.network.send_msg(this_msg)
        
    def start_periodic(self):
        msg = self.get_con_msg()
        self.task = self.network.bus_agent.send_periodic(msg, 0.50)

        assert isinstance(self.task, can.CyclicSendTaskABC)
    
    def stop_periodic(self):
        self.task.stop()