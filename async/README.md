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

