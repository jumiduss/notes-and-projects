
import asyncio
from typing import List

import time
 
import can
from can.notifier import MessageRecipient


def print_message(msg: can.Message) -> None:
    """Regular callback function. Can also be a coroutine."""
    print(msg)


async def main() -> None:
    """The main function that runs in the loop."""

    with can.Bus(  
        interface="socketcan", channel="vcan0", receive_own_messages=False
    ) as bus:
        reader = can.AsyncBufferedReader()

        listeners: List[MessageRecipient] = [
            reader,  # AsyncBufferedReader() listener
        ]
        
        # Create Notifier with an explicit loop to use for scheduling of callbacks
        loop = asyncio.get_running_loop()
        notifier = can.Notifier(bus, listeners, loop=loop)
        
        # Start sending first message
        period = bus.send_periodic(can.Message(arbitration_id=0x681, data=[0x0,0x0,0xC,0x0,0xF,0xF,0xE,0xE]), 0.5)

        t_0 = time.time()
        t_1 = t_0
        sent_msg = 0x00
        while True:
            # Wait for next message from AsyncBufferedReader
            msg = await reader.get_message()
            print(msg)
            
            if (time.time() - t_1) > 2:
                smsg = can.Message(arbitration_id=0x681, data=[0xA0,0xE1,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF])
                bus.send(msg=smsg)
                print(smsg)
                t_1 = time.time()
                
                if sent_msg == msg:
                    print("received")
                    
                sent_msg = smsg

            if (t_0 + 100) < time.time():
                break
            
        
        period.stop()
        print("Done!")

        # Clean-up
        notifier.stop()


if __name__ == "__main__":
    asyncio.run(main())