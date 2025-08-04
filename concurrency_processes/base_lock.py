from multiprocessing import Process, Value, Lock


def increment(counter, lock):
    for _ in range(100000):
        with lock:
            counter.value += 1


if __name__ == "__main__":
    counter = Value('i', 0)  # Shared integer
    lock = Lock()
    processes = [Process(target=increment, args=(counter, lock)) for _ in range(4)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("Final counter:", counter.value)
