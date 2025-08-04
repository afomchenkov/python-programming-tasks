from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def work(x):
    time.sleep(1)
    return x * 2


# Thread-based pool (for I/O)
with ThreadPoolExecutor() as executor:
    results = executor.map(work, [1, 2, 3])
    print(list(results))

# Process-based pool (for CPU)
with ProcessPoolExecutor() as executor:
    results = executor.map(work, [1, 2, 3])
    print(list(results))
