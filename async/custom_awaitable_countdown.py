import asyncio


class Countdown:
    def __init__(self, count):
        self.count = count

    def __await__(self):
        for i in range(self.count, 0, -1):
            print(f"{i}...")
            yield from asyncio.sleep(1).__await__()
        return "Done!"


async def main():
    result = await Countdown(3)
    print(result)

asyncio.run(main())
