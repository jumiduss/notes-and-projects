import can
from can.notifier import MessageRecipient
from typing import List
import asyncio
import time

async def main():
    with can.Bus("vcan0", "socketcan", bitrate=500000) as bus:
        
        msg = can.Message(arbitration_id=0x601, data=[0xE1,0x01,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF])
        period = bus.send_periodic(msg, 0.5)
        
        reader = can.AsyncBufferedReader()
        listeners: List[MessageRecipient] = [
            reader,  # AsyncBufferedReader() listener
        ]
        
        loop = asyncio.get_running_loop()
        notifier = can.Notifier(bus, listeners, loop=loop)
        
        t_0 = time.time()
        while True:
            msg = await reader.get_message()
            print(msg)
            
            
            if msg.data[0] == 0xA0:
                bus.send(msg)
            
            
            
            if (time.time() - t_0) > 100:
                break
        
        period.stop()
        notifier.stop()

if __name__ == "__main__":
    asyncio.run(main())