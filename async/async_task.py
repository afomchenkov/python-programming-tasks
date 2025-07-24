import asyncio

"""
asyncio.Task is an object that schedules and independently runs a coroutine.
It is a subclass of Future, which means it can be awaited.

Tasks are used to run coroutines concurrently, allowing for cooperative multitasking.
Tasks are created using asyncio.create_task() or asyncio.ensure_future().

A task is created from a coroutine and is responsible for executing it. It requires
a coroutine object, wraps coroutine, schedules it for execution, and provides a way to await its result.
Tasks can be cancelled, and they handle exceptions raised in the coroutine.
"""


async def task_coroutine():
    print("Task started")
    await asyncio.sleep(2)  # Simulate some work
    print("Task completed")
    return "Task finished successfully"


async def main():
    print('Main coroutine')
    """
    After the task has been created, we can check its status:
        - `task.done()` returns True if the task has finished executing.
        - `task.cancel()` can be used to cancel the task if it hasn't started yet.
        - `task.cancelled()` returns True if the task was cancelled.
        - `task.running()` returns True if the task is currently running.
        - `task.result()` retrieves the result of the task if it has completed successfully.
        - `task.exception()` retrieves any exception raised by the task.
        - `task.add_done_callback(callback)` allows you to register a callback that will be called
          when the task is done, passing the task as an argument to the callback.
    """
    task = asyncio.create_task(task_coroutine())
    print("Task created, running concurrently with main coroutine")
    await asyncio.sleep(1)
    print("Main coroutine is still running")

    try:
        print("Waiting for task to complete...")
        await task
        result = task.result()
    except asyncio.CancelledError:
        print("Task was cancelled")
    except Exception as e:
        print(f"Task raised an exception: {e}")
    else:
        print("Task completed successfully")

    print(f"Task result: {result}")

asyncio.run(main())
