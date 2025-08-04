from multiprocessing import Pool
import time


def square(x):
    time.sleep(1)  # Simulate work
    return x * x


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print("Results:", results)
