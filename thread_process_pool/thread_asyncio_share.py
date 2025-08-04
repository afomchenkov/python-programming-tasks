import asyncio
import threading
import queue
import time

# Thread-safe queue
shared_q = queue.Queue()

# Thread that produces data
def thread_producer():
    for i in range(5):
        shared_q.put(f"data-{i}")
        time.sleep(1)

# Async coroutine that consumes data
async def async_consumer():
    loop = asyncio.get_running_loop()
    for _ in range(5):
        data = await loop.run_in_executor(None, shared_q.get)
        print(f"[asyncio] Got from thread: {data}")

async def main():
    t = threading.Thread(target=thread_producer)
    t.start()
    await async_consumer()
    t.join()

asyncio.run(main())
