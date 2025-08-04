import time

# Sample data
nums = list(range(100_000))

# Using for loop
start = time.time()
squares_loop = []
for n in nums:
    squares_loop.append(n * n)
print("For loop:", time.time() - start)

# Using list comprehension
start = time.time()
squares_comp = [n * n for n in nums]
print("List comprehension:", time.time() - start)
