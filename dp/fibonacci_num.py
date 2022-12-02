from functools import lru_cache

@lru_cache(None)
def fibonacci_recurs(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recurs(n - 1) + fibonacci_recurs(n - 2)

# DP bottom-up solution
def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f

    return f_minus_1


if __name__ == '__main__':
    res = fibonacci(4)
    pass
