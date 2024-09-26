import random
import time
import matplotlib.pyplot as plt


def analyze_sort_performance(sizes, sort_func):
    times = []
    for size in sizes:
        input_data = [random.randint(0, size * 10) for _ in range(size)]
        start_time = time.perf_counter()
        sort_func(input_data.copy())
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times


def plot_sort_performance(sizes, times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker="o")
    plt.xlabel("Number of elements")
    plt.ylabel("Time (seconds)")
    plt.title("Bubble Sort Performance")
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()


def print_sort_results(sizes, times):
    print("\nBubble Sort Performance Results:")
    for i, size in enumerate(sizes):
        print(f"Size: {size}, Time: {times[i]:.6f} seconds")
