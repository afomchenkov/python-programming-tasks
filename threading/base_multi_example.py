import threading
import time

def print_numbers(name):
    for i in range(3):
        print(f"{name} printing {i}")
        time.sleep(1)

t1 = threading.Thread(target=print_numbers, args=("Thread 1",))
t2 = threading.Thread(target=print_numbers, args=("Thread 2",))

t1.start()
t2.start()

print("Main thread is running concurrently")

t1.join()
t2.join()
print("All threads done")
