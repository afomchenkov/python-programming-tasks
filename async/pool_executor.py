from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

"""
- Concurrency via threads
- Best for I/O-bound tasks (e.g., network requests, file I/O)
- All threads share the same memory space (no pickling required)
- Subject to the Global Interpreter Lock (GIL) — so not great for CPU-heavy tasks
"""

def fetch_url(url):
    # Simulate an I/O-bound task
    import requests
    return requests.get(url).status_code


urls = ["https://example.com", "https://google.com"]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch_url, urls)

for result in results:
    print(result)



"""
- Parallelism via separate processes
- Best for CPU-bound tasks (e.g., heavy computation)
- Each process runs in its own memory space — requires picklable functions and arguments
- Not subject to the GIL
"""


def compute_heavy(x):
    # Simulate CPU-bound work
    total = 0
    for i in range(10**6):
        total += i * x
    return total


with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(compute_heavy, [1, 2, 3, 4])

for result in results:
    print(result)
