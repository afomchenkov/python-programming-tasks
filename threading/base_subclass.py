import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print(f"{self.name} working...")
            time.sleep(1)

t = MyThread()
t.start()
t.join()
print("Thread completed")
