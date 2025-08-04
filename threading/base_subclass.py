import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for _ in range(3):
            print(f"{self.name} working...")
            time.sleep(1)


if __name__ == '__main__':
    t = MyThread()
    t.start()
    t.join()
    print("Thread completed")
