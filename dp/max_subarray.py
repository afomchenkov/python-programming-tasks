def max_subarr(nums: list[int]) -> list[int]:
    if len(nums) == 0:
        return []

    max_so_far = max_here = 0
    for num in nums:
        max_here = max(num, max_here + num)
        max_so_far = max(max_so_far, max_here)

    return max_so_far

if __name__ == '__main__':
    test_arr1 = [904, 40, 523, 12, -335, -385, -124, 481, -31]
    result1 = max_subarr(test_arr1)
    print(result1)
    pass
