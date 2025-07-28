import asyncio
from random import random

"""
create lock
lock = asyncio.Lock()
await lock.acquire()
# do something
lock.release()

# with context manager
async with lock:
    # do something
"""


"""
If two coroutines access a shared structure (like a file, list, or database connection), 
the interleaving caused by await can break assumptions about atomicity.
"""
# async def task(num, value):
#     print(f"Task {num} processing value: {value}")
#     await asyncio.sleep(random())
#     print(f"Task {num} finished")


async def task(lock, num, value):
    async with lock:
        print(f"Task {num} acquired lock, processing value: {value}")
        await asyncio.sleep(random())
        print(f"Task {num} released lock")


async def main():
    lock = asyncio.Lock()
    tasks = [task(lock, i, random()) for i in range(5)]
    await asyncio.gather(*tasks)
    print("All tasks completed")


if __name__ == "__main__":
    asyncio.run(main())
