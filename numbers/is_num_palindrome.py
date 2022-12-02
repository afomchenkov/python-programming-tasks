# True for 0, 1, 7, 11, 121, 333, 2147447412
# False for -1, 12, 100, 2147483647

import math


def is_palindrome(x: int) -> bool:
    if x <= 0:
        return False

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)
    for _ in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False

        x %= msd_mask    # remove the most significant digit of x
        x //= 10         # remove the least significant digit of x
        msd_mask //= 10

    return True

if __name__ == '__main__':
    assert(is_palindrome(111) == True)
