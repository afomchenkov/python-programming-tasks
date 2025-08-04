import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def blocking_io():
    time.sleep(2)
    return "blocking done"


async def main():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, blocking_io)
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
