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

