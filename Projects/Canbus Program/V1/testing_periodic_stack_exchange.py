import can
import time

# def receive(bus, message, signal):
#     # include dbc file
#     db = cantools.db.load_file(dbc_path)
#     for msg in bus:
#         if msg is not None and msg.arbitration_id == message.arbitration_id:
#             message_data = db.decode_message(msg.arbitration_id, msg.data)
#             signal_data = message_data.get(signal)
#             return signal_data


bus = can.Bus(channel="vcan0",interface="socketcan",bitrate=500000)
running = True
then = time.time()
with bus:    
    print("Starting to send a message every 200ms.")
    msg = can.Message(
        arbitration_id=0x681, data=[0xF0, 0x06, 0x0A, 0x01, 0xFF, 0xFF,0xFF,0xFF], is_extended_id=False
    )
    task = bus.send_periodic(msg, 0.20)

    assert isinstance(task, can.CyclicSendTaskABC)

    while running:
        for rec_msg in bus:
            print(rec_msg)
        now=time.time()
        if now > (then + 20):
            running = False
    
    task.stop()

    print("stopped cyclic send")