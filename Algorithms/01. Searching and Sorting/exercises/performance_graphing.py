import time
import matplotlib.pyplot as plt


def measure_execution_time(func, input_data):
    # as we are calling the binary search functions with a target as param now, we have to provide the target:
    target = len(input_data) // 2
    start_time = time.perf_counter()
    # for benchmarking testing purposes, we run the function 10000 times
    for i in range(10000):
        func(input_data, target)
    end_time = time.perf_counter()
    return end_time - start_time


def plot_performance(sizes, times, algorithm_names):
    plt.figure(figsize=(12, 6))
    for i, times_list in enumerate(times):
        plt.plot(sizes, times_list, marker="o", label=algorithm_names[i])
    plt.xlabel("Number of elements")
    plt.ylabel("Time (seconds)")
    plt.title("Performance Comparison")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()


def print_performance_results(sizes, times, algorithm_names):
    print("Performance Results:")
    for i, size in enumerate(sizes):
        print(f"Size: {size}")
        for j, alg_name in enumerate(algorithm_names):
            print(f"  {alg_name}: {times[j][i]:.6f} seconds")
        print()


def run_performance_analysis(algorithms, sizes, generate_input, algorithm_names):
    times = [[] for _ in algorithms]

    for size in sizes:
        input_data = generate_input(size)
        for i, alg in enumerate(algorithms):
            execution_time = measure_execution_time(alg, input_data)
            times[i].append(execution_time)

    plot_performance(sizes, times, algorithm_names)
    print_performance_results(sizes, times, algorithm_names)
