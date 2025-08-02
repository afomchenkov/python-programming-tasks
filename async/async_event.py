import asyncio
from random import random

"""
An Event object is a synchronization primitive that can be used to signal between coroutines.
It allows one coroutine to notify one or more other coroutines that an event has occurred.

- an Event object has an internal flag that can be set or cleared
- when the flag is set, any coroutine that is waiting for the event will be notified
- when the flag is cleared, any coroutine that is waiting for the event will be blocked until
  the flag is set again
- it is useful for coordinating the execution of multiple coroutines, especially when one
  coroutine needs to wait for another coroutine to complete before proceeding.
- it can be used to implement a simple signaling mechanism between coroutines.
"""

async def task(event, num):
    print(f"Task {num} waiting for event")
    await event.wait()  # Wait until the event is set
    await asyncio.sleep(random())
    print(f"Task {num} proceeding after event is set")

async def main():
    event = asyncio.Event()
    tasks = [asyncio.create_task(task(event, i)) for i in range(5)]

    print("Main suspending...")
    await asyncio.sleep(0)

    print("Main setting the event")
    event.set()

    _ = await asyncio.wait(tasks)
    print("All tasks completed")

if __name__ == "__main__":
    asyncio.run(main())
    print("Program finished.")