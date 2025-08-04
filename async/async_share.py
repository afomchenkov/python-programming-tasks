import asyncio
from threading import Thread

async def async_producer(q):
    for i in range(5):
        await q.put(f"item-{i}")
        await asyncio.sleep(0.5)

def thread_consumer(q):
    while True:
        item = asyncio.run_coroutine_threadsafe(q.get(), asyncio.get_event_loop()).result()
        print(f"[thread] Consumed: {item}")
        if item == "item-4":
            break

async def main():
    q = asyncio.Queue()

    # Start consumer thread
    consumer_thread = Thread(target=thread_consumer, args=(q,))
    consumer_thread.start()

    await async_producer(q)
    consumer_thread.join()

asyncio.run(main())
