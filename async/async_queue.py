import asyncio
from random import random

"""
A queue can be used to share data between coroutines.
It is a thread-safe data structure that allows multiple producers and consumers to
communicate with each other.
It is useful for implementing producer-consumer patterns, where one or more coroutines
produce data and one or more coroutines consume it.
"""


class CheckQueue():
    def __init__(self):
        pass

    async def run(self):
        print("Queue is running")

        async def producer(queue):
            print("Producer started")
            for i in range(5):
                item = f"item-{i}"
                await queue.put(item)
                print(f"Produced {item}")
                await asyncio.sleep(random())
            await queue.put(None)  # Signal consumer to exit
            print("Producer finished")

        async def consumer(queue):
            print("Consumer started")
            while True:
                item = await queue.get()
                if item is None:
                    print("Consumer received exit signal")
                    break
                print(f"Consumed {item}")
                await asyncio.sleep(random())

        queue = asyncio.Queue()

        # await asyncio.create_task(producer(queue))
        # await asyncio.create_task(consumer(queue))

        await asyncio.gather(
            producer(queue),
            consumer(queue)
        )
        print("Queue processing complete")


async def main():
    queue = asyncio.Queue(maxsize=100)

    async def producer():
        for i in range(5):
            await queue.put(i)
            print(f"Produced {i}")
            await asyncio.sleep(1)

    async def consumer():
        while True:
            item = await queue.get()
            if item is None:  # Exit condition
                break
            print(f"Consumed {item}")
            await asyncio.sleep(2)
            queue.task_done()

    # Create producer and consumer tasks
    prod_task = asyncio.create_task(producer())
    cons_task = asyncio.create_task(consumer())

    await prod_task
    await queue.join()  # Wait until all items are processed
    await cons_task  # Signal consumer to exit
    await queue.put(None)  # Send exit signal to consumer
    print("All tasks completed")

if __name__ == "__main__":
    asyncio.run(main())
