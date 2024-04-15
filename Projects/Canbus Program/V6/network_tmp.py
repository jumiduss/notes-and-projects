import can 
import asyncio


msg_clock = 0x0

async def send_msg(arb_id: int, msg_data: list, bus: can.Bus, is_clocked: bool):
    global msg_clock
    if is_clocked:
        msg_data[1] = msg_clock
    
    msg = can.Message(arbitration_id=arb_id, data=msg_data)
    bus.send(msg)


async def main():
    
    bus = can.Bus(channel='van0', interface='socketcan', bitrate=500000)





if __name__ == '__main__':
    
    asyncio.run(main())