# Async IO

## Coroutine - a function that can be suspended and resumed

```txt
- Cooperative multitasking - task itself decides when it's being executed, resumed
- Preemptive multitasking - involves the OS to choose what threads to suspend/resume and when
```

## Coroutine/Routine/Subroutine

```txt
- Routine/Subroutine - refer to the same thing, a routine has subroutine
- Routine - is a program
- Subroutine - is a function in the program

A coroutine is an extension of a subroutine:
- they both are discrete named modules of expressions
- they both can take arguments, or not
- they both can return a value, or not

The main difference is that a coroutine can suspend/resume its execution many
times before returning and exiting.
Coroutine can execute another coroutine/subroutine, it must suspend its execution
and allow another coroutine to run.
```

Python provides Executor-based thread pools and process pools in the ThreadPoolExecutor
and ProcessPoolExecutor classes.


## asyncio

Python provides coroutines as first-class objects and the asyncio module
supports asynchronous programming.

The module provides utility functions and classes to assist in creating
and managing asynchronous tasks and performing non-blocking I/O with
sockets and subprocesses. It provides the event loop required to execute
coroutines.

```python
# define coroutine function
import asyncio

async def custom_coro():
    # await another coroutine
    await another_coro()

# calling a coroutine function will return a coroutine object
# which is an instance of coroutine class

# start an asyncio program
asyncio.run(main())
```

## When to use asyncio

- non-blocking I/O with subprocesses or socket connections
- the benefit of coroutines outweighs the benefits of threads and processes
- the async programming paradigm is preferred or required

Asyncio is specifically designed for non-blocking I/O with subprocesses and TCP
socket connections.
If an app requires a large number of concurrent socket or subprocess tasks, then
asyncio is an obvious choice.

- executing and checking the results of many commands on a system
- making and managing many socket connections
- serving access to many client socket connections



## Examples of TCP-based database protocols

```txt
| Database             | Protocol          | Default Port | TCP-based |
| -------------------- | ----------------- | ------------ | --------- |
| PostgreSQL           | PostgreSQL binary | 5432         | ✅ Yes     |
| MySQL                | MySQL protocol    | 3306         | ✅ Yes     |
| MongoDB              | MongoDB Wire      | 27017        | ✅ Yes     |
| Redis                | RESP              | 6379         | ✅ Yes     |
| Microsoft SQL Server | TDS               | 1433         | ✅ Yes     |
```

```txt
queue.Queue + run_in_executor	Threads → asyncio	✅
asyncio.Queue + run_coroutine_threadsafe	asyncio → threads	✅
threading.Lock	Shared memory protection	✅
asyncio.run_in_executor	Run sync/blocking code in thread	✅
```
