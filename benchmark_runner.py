import time
import random
import sys
# Increase recursion depth for unoptimized quick sort on sorted arrays if necessary
sys.setrecursionlimit(5000)

from sorting_engine import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

def run_benchmarks():
    sizes = [100, 500, 2000]
    print(f"{'Algorithm':<18} | {'N=100 (sec)':<12} | {'N=500 (sec)':<12} | {'N=2000 (sec)':<12}")
    print("-" * 65)

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    for name, func in algorithms.items():
        row_str = f"{name:<18}"
        for size in sizes:
            # Generate a fresh randomized block of order data
            test_data = [random.randint(1, 10000) for _ in range(size)]
            
            start_time = time.perf_counter()
            func(test_data.copy())
            end_time = time.perf_counter()
            
            row_str += f" | {end_time - start_time:<12.5f}"
        print(row_str)

if __name__ == "__main__":
    print("Gathering data on formal performance properties...\n")
    run_benchmarks()
