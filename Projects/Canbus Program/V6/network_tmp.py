import can


socket_bus = can.Bus(interface='socketcan', channel='can1')

with socket_bus as bus:
    for msg in bus:
        print(msg.data)