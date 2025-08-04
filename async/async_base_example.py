import asyncio
import threading
import time
from random import random


async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay} sec")


def start_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def main():
    print('before coroutine')

    await asyncio.gather(
        *[asyncio.create_task(task(f'test {i}', random())) for i in range(5)]
    )
    # await task('test1', 1)
    # await task('test2', 1.1)
    # await task('test3', .9)
    print('after coroutine')


if __name__ == "__main__":
    new_loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_event_loop, args=(new_loop,), daemon=True)
    t.start()

    asyncio.run_coroutine_threadsafe(main(), new_loop)

    for i in range(5):
        print(f"[Main Thread] Working... {i}")
        time.sleep(0.8)
