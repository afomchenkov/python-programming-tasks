import asyncio
from concurrent.futures import ProcessPoolExecutor


def cpu_heavy(x):
    return sum(i*i for i in range(x))


async def main():
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_heavy, 10**6)
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
