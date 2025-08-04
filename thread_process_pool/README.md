# Treading/Processing

```txt
trio	Structured async concurrency with better ergonomics
curio	Lightweight coroutine framework (no asyncio)
gevent	Greenlets for coroutine-based concurrency using monkey-patching
joblib	Parallel processing for scientific computing
ray	Distributed computing on clusters or locally
dask	Scalable analytics and parallel data pipelines
```

```txt
I/O-bound (web, disk)	asyncio, threading
CPU-bound (heavy math)	multiprocessing, ProcessPoolExecutor
Many small tasks	asyncio, trio, gevent
Distributed processing	ray, dask
Async + Blocking I/O	asyncio + run_in_executor
```
