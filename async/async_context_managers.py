"""
an async iterator:
- is an object that implements the __aiter__() and __anext__() methods
- can be used in an async for loop
- can be used with the await keyword

async context managers:
- an object that implements __aenter__() and __aexit__() methods
- can be used with the async with statement
- allows for asynchronous setup and teardown operations

class AsyncContextManager:
    async def __aenter__(self):
        print("Entering async context")
        await asyncio.sleep(0.5)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await asyncio.sleep(0.5)
        print("Exiting async context")


async with AsyncContextManager() as manager:
    print("Inside async context")

manager = await AsyncContextManager()
try:
    await manager.__aenter__()
    # do something with the resource
finally:
    await manager.__aexit__(None, None, None)
    await manager.close()


context manager:
- implements __enter__() and __exit__() methods
- can be used with the with statement
- allows for setup and teardown operations
- can be used to manage resources like files, network connections, etc.
- ensures that resources are properly cleaned up after use, even if an error occurs
- can be used to manage resources like files, network connections, etc.

manager = ContextManager()
try:
    manager.__enter__()
    # do something with the resource
finally:
    manager.__exit__(None, None, None)

- can be used to manage resources like files, network connections, etc.
"""

import asyncio


class AsyncIterator():
    def __init__(self, count):
        self.count = count
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.count:
            await asyncio.sleep(.3)
            self.current += 1
            return self.current
        else:
            raise StopAsyncIteration


async def main():
    it = AsyncIterator(5)
    # result = await anext(it)
    # print(f"First item: {result}")
    async for result in it:
        print(f"Item: {result}")

    results = [item async for item in AsyncIterator(3)]
    print(results)

    async def async_generator():
        for i in range(5):
            await asyncio.sleep(0.5)
            yield i

    it = async_generator()
    async for item in it:
        print(f"Async generator item: {item}")
        
    results = [item async for item in async_generator()]
    print(f"Async generator results: {results}")

if __name__ == "__main__":
    def generator():
        for i in range(5):
            yield i
        # yield from range(5)

    gen = generator()
    result = next(gen)
    print(f"First item from generator: {result}")

    results = [i for i in generator()]

    asyncio.run(main())
