from multiprocessing import Process
import time


def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")


if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    print("Main process continues while worker runs")
    p.join()
    print("Main process exiting")
