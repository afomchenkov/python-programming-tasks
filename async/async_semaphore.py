import asyncio
from random import random

"""
The Semaphore object must be configured when it is created to set the limit
on the interanl counter.
This limit will match the number of concurrent coroutines that can
hold the semaphore at the same time.

- each time a coroutine acquires the semaphore, the internal counter is decremented
- each time a coroutine releases the semaphore, the internal counter is incremented
- if the internal counter reaches zero, any coroutine that tries to acquire the semaphore
  will be block until another coroutine releases the semaphore
- if the internal counter is greater than zero, the coroutine will acquire the semaphore
- the semaphore can be used to limit the number of concurrent tasks that can run at the same
  time, which is useful for controlling resource usage or preventing overloading of external
  systems.
"""


async def task(semaphore, number):
    async with semaphore:
        print(f"Task {number} started")
        await asyncio.sleep(random())
        print(f"Task {number} finished")


async def main():
    print("Starting async tasks...")

    semaphore = asyncio.Semaphore(2)

    tasks = [asyncio.create_task(task(semaphore, i)) for i in range(5)]
    _ = await asyncio.wait(tasks)

    # use semaphore with context manager
    # async with semaphore:
    #     print("Semaphore acquired, running async tasks...")
    #     # Simulate some async work
    #     await asyncio.sleep(1)
    #     print("Async tasks completed.")

    # await semaphore.acquire()
    # semaphore.release()

    # Simulate some async work
    await asyncio.sleep(1)
    print("Async tasks completed.")


if __name__ == "__main__":
    asyncio.run(main())
    print("Program finished.")
