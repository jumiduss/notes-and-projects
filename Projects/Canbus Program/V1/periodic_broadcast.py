import can
# import time
bus = can.interface.Bus(interface='socketcan',channel='vcan0',bitrate=500000)

with bus:
    msg = can.Message(
        arbitration_id=0x681,
        data=[0xF5, 0x00, 0xA1, 0x01, 0xFF, 0xFF, 0xFF, 0xFF],
        is_extended_id=False
    )
    round = 0
    running = True
    while running:
        task = bus.send_periodic(msg, 0.20)
        assert isinstance(task, can.CyclicSendTaskABC)
        print("Sent")
        # time.sleep(0.50)
        # try: 
        #     bus.send(msg)
        #     print("Message Sent")
        # except can.CanError:
        #     print("Message NOT Sent")
        if round > 5:
            break
        else:
            round+=1
            
    task.stop()
