import asyncio
from aioconsole import ainput

BOUND = 10**5

class Collatz:
    
    def __init__(self):
        self.start = 2
    
    async def count_steps(self, start_value):
        steps = 0
        n = start_value
        while n > 1:
            if n % 2:
                n = n * 3 + 1
            else:
                n = n // 2
        
        return steps

    def __aiter__(self):
        return self

    async def __anext__(self):
        steps = await self.count_steps(self.start)
        self.start += 1
        if self.start == BOUND:
            raise StopAsyncIteration
        return steps


async def length_counter(target):
    count = 0
    async for steps in Collatz():
        if steps == target:
            count += 1
    return count

