import asyncio
import threading

shared_data = []
data_lock = threading.Lock()

def thread_task():
    with data_lock:
        shared_data.append("from thread")

async def async_task():
    await asyncio.sleep(1)
    with data_lock:
        shared_data.append("from async")

async def main():
    t = threading.Thread(target=thread_task)
    t.start()
    await async_task()
    t.join()
    print(shared_data)

asyncio.run(main())
