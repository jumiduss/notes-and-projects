# 1. Start with any positive integer n.
# 2. If n is even, the next term in the sequence is n / 2.
# 3. If n is odd, the next term in the sequence is 3n+1.
# 4. If n is 1, stop.

# Code added for asynchrony is comment wrapped with:
#*
# CODE HERE (NO COMMENT)
#* 
# or I/O asynchrony:
#**
# CODE HERE (NO COMMENT)
#**
 
# Adding asynchrony relies on noticing where the program is waiting, or bound 
#   by a specific task. 
#   In this program, we are delayed by the CPU's processing speed, and user's inputs.
#       This is called  CPU-bound, and I/O-bound respectively.

# Simple co-routines run until they hit a yield statement, then wait for data 
#    to be sent to the object with send().
# Native co-routines (AKA co-routine functions) can be paused and resumed
#    to achieve multi-tasking-like behavior.
# To achieve asynchrony: 
# 1. You declare a native co-routine function by adding async before the def of a function.
# 2. A co-routine function returns a native-co-routine object, called an awaitable.
# 3. Awaitables are called using "await" which acts like a "yield from" statement. 
# 4. Await can only be used INSIDE an awaitable.
# 5. Functions should only be turned into a co-routine when it:
#       calls another awaitable
#       performs an IO-bound task
#       when it's intended to run concurrently with another awaitable
# 
# The aioconsole provides functionality for allowing "true-er" asynchrony 
#    for processes like input(). 

#*
import asyncio
#*
#**
from aioconsole import ainput
#**

#Defining the upper bounds of the number we can use.
BOUND = 10**5

def collatz(n):
    #*
    # This function returns almost instantly, so it's neither an awaitable, 
    #    or runs concurrently.
    #*
    """Finds the number of steps in a single Collatz Sequence."""
    
    steps = 0
    while n > 1:
        if n % 2:
            n = n * 3 + 1
        else:
                n /= 2
        
        steps += 1
    return steps

#*
async def length_counter(target):
    # This function IS CPU-intensive, so should be run concurrently.
    #*
    """Tracks the number of correct guesses on the target sequence's length"""
    
    count = 0
    
    for i in range(2, BOUND):
        if collatz(i) == target:
            count += 1
        #*
        # The async + await turns this function into a co-routine function.
        # If await is never used, it will never be paused.
        await asyncio.sleep(0)
        #*
    return count

#*
async def get_input(prompt) -> int:
    # This function IS I/O-bound, thus WAITS for a user input.
    # Because we wait on a user input, we don't need an await statement.
    #*
    """Requests positive integer from the user. Returns a positive integer"""
    
    while True:
        # n = input(prompt)
        #**
        n = await ainput(prompt)
        #**
        try:
            n = int(n)
        except ValueError:
            print("Value must be an integer.")
        
        if n <= 0:
            print("Value must be positive.")
        else:
            return n

#*
async def main():
    # We MUST call a co-routine function from another co-routine function.
    # Even if main() is not asynchronous, it must have async to call and run 
    #    get_input() as a co-routine.
    # Note, length_counter() can be executed manually and synchronously,
    #    so we must call an asynchronous function specially to act as intended. 
    # Two ways to run co-routine functions:
    #    Directly awaiting them.
    #    Scheduling them as tasks.
    #*
    print("Collatz Sequence Calculator")
    
    #target = get_input("Collatz sequence length to search for: ")
    
    #*
    # The guess awaitable must be called before the program can do anything.
    #    This is where we get the number to pass to the CPU-bound function.
    #    This means we can accept/allow the program delay from the user's input. 
    # Calling get_input with await blocks the program until the response is made.
    target = await get_input("Collatz sequence length to search for: ")
    #*
    
    print(f"Searching in range1-{BOUND}")
    
    #*
    # We schedule the co-routines as tasks so that as soon as main() is waiting,
    #    we allow another task to process in turns until length_counter() returns.
    #    The program then waits for the guess to be entered if it hasn't been
    #    submitted before the end of length_counter()'s execution.
    
    # length_counter_task = asyncio.create_task(length_counter(target))
    # guess_task = asyncio.create_task(
    #     get_input("How many times do you think it will appear? ")
    # )
    # count = await length_counter_task
    # guess = await guess_task
    
    #Simplifying the above code:
    (guess, count) = await asyncio.gather(
        get_input("How many times do you think it will appear? "),
        length_counter(target)
    )
    # Once we have the input, we can run the calculation while waiting for
    #    the user's count guess. 
    #    
    #*
    
    # count = length_counter(target)
    # guess = get_input("How many times do you think it will appear? ")
    
    if guess == count:
        print("Exactly right! I'm amazed.")
    elif abs(guess - count) < 100:
        print(f"You're close! It was {count}.")
    else:
        print(f"Nope. It was {count}.")

if __name__ == "__main__":
    # main()
    
    #*
    # Since only co-routines can be called with await, we must use an event loop
    #    to allow main() to run with co-routines.
    
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    
    # If you want a shorter way to perform the above task:
    asyncio.run(main())
    #*