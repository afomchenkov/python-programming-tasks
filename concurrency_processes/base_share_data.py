from multiprocessing import Process, Queue

def worker(q):
    q.put("Message from child")


if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print("Got from queue:", q.get())
    p.join()
