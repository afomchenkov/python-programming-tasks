from multiprocessing import Process
import time


def task(name):
    for i in range(3):
        print(f"{name} says {i}")
        time.sleep(1)


if __name__ == "__main__":
    p1 = Process(target=task, args=("Process A",))
    p2 = Process(target=task, args=("Process B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Both processes done")
