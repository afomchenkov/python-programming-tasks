import asyncio
from random import random


async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay} sec")


async def main():
    print('before coroutine')

    await asyncio.gather(
        *[task(f'test {i}', random()) for i in range(5)]
    )
    # await task('test1', 1)
    # await task('test2', 1.1)
    # await task('test3', .9)
    print('after coroutine')


if __name__ == "__main__":
    
    asyncio.run(main())
