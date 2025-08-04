from multiprocessing import Process, Manager

def update(shared_dict):
    shared_dict["count"] += 1

if __name__ == "__main__":
    with Manager() as manager:
        shared = manager.dict({"count": 0})
        processes = [Process(target=update, args=(shared,)) for _ in range(5)]

        for p in processes:
            p.start()
        for p in processes:
            p.join()

        print("Final count:", shared["count"])
