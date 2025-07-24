import time
from multiprocessing import Pool
from threading import Thread


def cpu_task(x):
    count = 0
    for _ in range(10_000_000):
        count += x * x
    return count


def run_multiprocessing():
    with Pool(processes=4) as pool:
        results = pool.map(cpu_task, [1, 2, 3, 4])
    return results


def run_multithreading():
    threads = []
    for x in [1, 2, 3, 4]:
        t = Thread(target=cpu_task, args=(x,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    start = time.time()
    run_multiprocessing()
    print("Multiprocessing took:", time.time() - start)

    start = time.time()
    run_multithreading()
    print("Multithreading took:", time.time() - start)
