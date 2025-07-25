import asyncio


async def coro1():
    print("Coro1 started")
    await asyncio.sleep(1)
    print("Coro1 finished")
    return "Coro1 result"


async def coro2():
    print("Coro2 started")
    await asyncio.sleep(2)
    print("Coro2 finished")
    return "Coro2 result"


async def task(i):
    print(f"Task {i} started")
    await asyncio.sleep(1)
    print(f"Task {i} finished")
    return f"Task {i} result"


async def main():
    print("Starting event loop")
    """
    If coroutines are provided to gather(), they are wrapped in a Task
    object automatically.
    The gather() function runs the coroutines concurrently and returns a Future
    that resolves when all the coroutines are done.
    If you want to run multiple coroutines concurrently, you can
    use asyncio.gather().
    """

    coros = [coro1(), coro2()]
    values = await asyncio.gather(*coros)
    # create many coroutines
    # values = await asyncio.gather(*(coro1() for _ in range(10)))
    # coros = [task_coro(i) for i in range(10)]
    print("Event loop finished")
    print("Results:", values)

    # create many tasks - asyncio.wait()
    tasks = [asyncio.create_task(task(i)) for i in range(10)]
    done, pending = await asyncio.wait(tasks, timeout=5)
    print("Tasks completed", done)
    print("Pending tasks:", pending)

    try:
        # create wait coroutine
        wait_coro = asyncio.wait(
            tasks,
            return_when=asyncio.ALL_COMPLETED,
            timeout=5,
        )
        done, pending = await wait_coro
    except asyncio.TimeoutError:
        print("Wait coroutine timed out")
    except Exception as e:
        print(f"Wait coroutine raised an exception: {e}")


if __name__ == "__main__":
    asyncio.run(main())
