import asyncio
from random import random

"""
asyncio.Condition objects are synchronization primitives that can be used to block a coroutine
until a certain condition is met. They are useful for coordinating the execution of
multiple coroutines, especially when one coroutine needs to wait for another coroutine
to complete before proceeding.

- a Condition object has an internal lock that is used to synchronize access to the condition
- when a coroutine calls the wait() method on a Condition object, it releases the internal lock
  and blocks until another coroutine calls the notify() or notify_all() method on the Condition object
- when a coroutine calls the notify() method, it wakes up one of the coroutines that
  are waiting on the Condition object
- when a coroutine calls the notify_all() method, it wakes up all of the coroutines
  that are waiting on the Condition object
- it is useful for implementing a simple signaling mechanism between coroutines.
- it can be used to implement a producer-consumer pattern, where one or more coroutines
  produce data and one or more coroutines consume it.


- coroutine-safe queues to share data between coroutines
- mutex locks to protect critical sections from race conditions
- semaphores to limit concurrent access to a resource for coroutines
- event signal to notify coroutines when a certain condition is met
- coordinate coroutines with wait and notify using condition variables
"""


async def task(condition, work_list, i):
    await asyncio.sleep(1)

    work_list.append(i + 1)

    print("Task sending notification")
    async with condition:
        condition.notify()


async def main():
    condition = asyncio.Condition()
    work_list = []

    print("Main waiting for notification")
    async with condition:
        _ = [asyncio.create_task(task(condition, work_list, i)) for i in range(3)]
        await condition.wait()

    print(f"Got notification, work_list: {work_list}")


if __name__ == "__main__":
    asyncio.run(main())
    print("Done")
