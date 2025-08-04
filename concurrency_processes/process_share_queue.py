from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello from worker")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # Read from queue
    p.join()
