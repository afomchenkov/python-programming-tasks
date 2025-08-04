from multiprocessing import Process, Value, Array

def worker(val, arr):
    val.value += 1
    for i in range(len(arr)):
        arr[i] *= 2

if __name__ == "__main__":
    num = Value('i', 10)  # 'i' = integer
    nums = Array('i', [1, 2, 3])

    p = Process(target=worker, args=(num, nums))
    p.start()
    p.join()

    print("Value:", num.value)
    print("Array:", nums[:])
