from performance_graphing_bubble import (
    analyze_sort_performance,
    plot_sort_performance,
    print_sort_results,
)


def bubble_sort(lst):
    n = len(lst)
    needs_sorting = False

    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                needs_sorting = True

        if not needs_sorting:
            break

    return lst


if __name__ == "__main__":
    sizes = [10, 100, 1000, 10000]
    times = analyze_sort_performance(sizes, bubble_sort)
    print_sort_results(sizes, times)
    plot_sort_performance(sizes, times)
