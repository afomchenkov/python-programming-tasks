import asyncio
import time

"""
asyncio.to_thread() is a utility function that allows you to run a synchronous function in an asyncio event loop.

It is particularly useful for running blocking I/O operations without blocking the event loop itself.
This is especially important in an asynchronous context where you want to maintain responsiveness.
It runs the synchronous function in a separate thread and returns a Future that resolves with the result of the function.
This allows you to use synchronous code in an asynchronous program without blocking the event loop.

It'll take a function call and execute it in a new thread, separate from the thread that is
executing the asyncio event loop.

Specifically designed for execute blocking I/O functions, not CPU-bound tasks that can also
block the asyncio event loop.
Treat a blocking function call as a coroutine and execute asynchronously using thread-based
concurrency instead of coroutine-based concurrency.
"""


def blocking_task():
    print("Blocking task started")
    time.sleep(2)  # Simulate a blocking I/O operation
    print("Blocking task finished")
    return "Blocking task result"


async def background():
    while True:
        print("Background task running")
        await asyncio.sleep(1)


async def main():
    print("Starting main coroutine")
    _ = asyncio.create_task(background())
    coro = asyncio.to_thread(blocking_task)
    await coro
    print("Main coroutine finished")

if __name__ == "__main__":
    asyncio.run(main())
