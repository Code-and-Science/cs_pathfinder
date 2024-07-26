import random
import time
import matplotlib.pyplot as plt
import cProfile
import pstats
import io

def generate_list_sequential(size):
    return list(range(size))

def binary_search_iterative(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(lst, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search_recursive(lst, target, mid + 1, right)
    else:
        return binary_search_recursive(lst, target, left, mid - 1)

def measure_search_time(search_func, lst, target):
    start_time = time.perf_counter()
    if search_func.__name__ == 'binary_search_recursive':
        search_func(lst, target, 0, len(lst) - 1)
    else:
        search_func(lst, target)
    end_time = time.perf_counter()
    return end_time - start_time

def profile_search(search_func, lst, target):
    pr = cProfile.Profile()
    if search_func.__name__ == 'binary_search_recursive':
        pr.runcall(search_func, lst, target, 0, len(lst) - 1)
    else:
        pr.runcall(search_func, lst, target)
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    return s.getvalue()

# Sizes to test
sizes = [10, 100, 1000, 10000, 100000, 1000000]

# Measure performance for different list sizes
iterative_times = []
recursive_times = []

for size in sizes:
    lst = generate_list_sequential(size)
    target = random.randint(0, size - 1)
    
    iterative_times.append(measure_search_time(binary_search_iterative, lst, target))
    recursive_times.append(measure_search_time(binary_search_recursive, lst, target))

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(sizes, iterative_times, marker='o', label='Iterative')
plt.plot(sizes, recursive_times, marker='s', label='Recursive')
plt.xlabel('Number of elements')
plt.ylabel('Time (seconds)')
plt.title('Binary Search Performance: Iterative vs Recursive')
plt.legend()
plt.grid(True)
plt.show()

# Print the results
print("Performance Results:")
for size, it_time, rec_time in zip(sizes, iterative_times, recursive_times):
    print(f"Size: {size:,}")
    print(f"  Iterative: {it_time:.6f} seconds")
    print(f"  Recursive: {rec_time:.6f} seconds")
    print()

# Detailed profiling for the largest size
largest_size = sizes[-1]
lst = generate_list_sequential(largest_size)
target = random.randint(0, largest_size - 1)

print(f"\nDetailed Profiling for size {largest_size:,}:")
print("\nIterative Binary Search:")
print(profile_search(binary_search_iterative, lst, target))
print("\nRecursive Binary Search:")
print(profile_search(binary_search_recursive, lst, target))
