import threading
import time

def worker():
    print("Thread starting")
    time.sleep(2)
    print("Thread finished")


if __name__ == '__main__':
    t = threading.Thread(target=worker)
    t.start()

    # Main thread continues
    print("Main thread is free to do other things")
    t.join()  # Wait for the thread to finish
    print("Main thread exiting")
