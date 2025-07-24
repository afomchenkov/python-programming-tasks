import asyncio


class CustomSleep:
    def __init__(self, delay):
        self.delay = delay

    def __await__(self):
        print(f"CustomSleep: sleeping for {self.delay} seconds...")
        # Delegate to asyncio.sleep()'s awaitable
        return asyncio.sleep(self.delay).__await__()


async def main():
    print("Before custom sleep")
    await CustomSleep(2)
    print("After custom sleep")

asyncio.run(main())
