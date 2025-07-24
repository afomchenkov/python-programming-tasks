import asyncio


class MyAsyncOperation:
    def __init__(self, delay: float, result: str):
        self.delay = delay
        self.result = result
        self._loop = asyncio.get_event_loop()

    def __await__(self):
        future = self._loop.create_future()

        def _complete_later():
            print(f"[MyAsyncOperation] Resolving after {self.delay}s")
            future.set_result(self.result)

        # Schedule completion after delay
        self._loop.call_later(self.delay, _complete_later)

        # Return awaitable future
        return future.__await__()


async def main():
    print("Waiting for custom async operation...")
    result = await MyAsyncOperation(2, "✅ Done")
    print(f"Result: {result}")

asyncio.run(main())
