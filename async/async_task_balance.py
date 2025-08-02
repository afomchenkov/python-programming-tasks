import asyncio
import random

balance = 0


async def add(lock):
    global balance
    async with lock:
        for _ in range(1000):
            tmp = balance
            await asyncio.sleep(random.uniform(0, 0.0001))
            tmp += 1
            await asyncio.sleep(random.uniform(0, 0.0001))
            balance = tmp


async def subtract(lock):
    global balance
    async with lock:
        for _ in range(1000):
            tmp = balance
            await asyncio.sleep(random.uniform(0, 0.0001))
            tmp -= 1
            await asyncio.sleep(random.uniform(0, 0.0001))
            balance = tmp


async def main():
    global balance
    balance = 0
    lock = asyncio.Lock()
    tasks = [add(lock) for _ in range(3)] + [subtract(lock) for _ in range(3)]
    random.shuffle(tasks)
    await asyncio.gather(*tasks)
    print(f"Final balance: {balance}")


if __name__ == "__main__":
    for i in range(5):
        print(f"Run {i + 1}:")
        asyncio.run(main())

