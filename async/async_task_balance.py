import asyncio
import random

balance = 0


async def add():
    global balance
    for _ in range(10000):
        tmp = balance
        await asyncio.sleep(random.uniform(0, 0.001))
        tmp = tmp + 1
        await asyncio.sleep(random.uniform(0, 0.001))
        balance = tmp

async def subtract():
    global balance
    for _ in range(10000):
        tmp = balance
        await asyncio.sleep(random.uniform(0, 0.001))
        tmp = tmp - 1
        await asyncio.sleep(random.uniform(0, 0.001))
        balance = tmp
        

# async def add():
#     global balance
#     for _ in range(10000):
#         async with lock:
#             tmp = balance
#             await asyncio.sleep(0)
#             tmp += 1
#             await asyncio.sleep(0)
#             balance = tmp

async def main():
    
    tasks = [add() for _ in range(2)] + [subtract() for _ in range(2)]
    random.shuffle(tasks)  # prevent grouping
    await asyncio.gather(*tasks)

    print(f"Final balance: {balance}")


if __name__ == "__main__":
    asyncio.run(main())
    print("Main: Done")
