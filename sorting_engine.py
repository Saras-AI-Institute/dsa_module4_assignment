"""
Module 4: Sorting Engine Optimization
Implement core sorting algorithms to sort lists in ascending order.
Do NOT use Python's built-in .sort() or sorted().
"""

# =========================================================================
# QUADRATIC SORTING ALGORITHMS O(n^2)
# =========================================================================

def bubble_sort(arr: list) -> list:
    """
    TODO: Implement Bubble Sort.
    1. Use nested loops to compare adjacent elements.
    2. If arr[j] > arr[j+1], swap them.
    3. Return arr.
    """
    # YOUR CODE HERE
    pass

def insertion_sort(arr: list) -> list:
    """
    TODO: Implement Insertion Sort.
    1. Loop from i = 1 to len(arr)-1.
    2. Store current element as `key = arr[i]` and `j = i - 1`.
    3. While j >= 0 and arr[j] > key: shift arr[j] to the right (arr[j+1] = arr[j]), then decrement j.
    4. Insert key into its correct spot: arr[j+1] = key.
    5. Return arr.
    """
    # YOUR CODE HERE
    pass

# =========================================================================
# LOG-LINEAR SORTING ALGORITHMS O(n log n)
# =========================================================================

def merge_sort(arr: list) -> list:
    """
    TODO: Implement Merge Sort (Divide and Conquer).
    1. Base case: if len(arr) <= 1, return arr.
    2. Split array into left and right halves.
    3. Recursively call merge_sort on both halves.
    4. Merge the two sorted halves into a single sorted list and return it.
    """
    # YOUR CODE HERE
    pass

def quick_sort(arr: list) -> list:
    """
    TODO: Implement Quick Sort.
    1. Base case: if len(arr) <= 1, return arr.
    2. Choose a pivot (e.g., the middle element or last element).
    3. Partition elements into three lists: 
       - smaller than pivot
       - equal to pivot
       - greater than pivot
    4. Recursively sort smaller and greater lists, then combine with equal list.
    """
    # YOUR CODE HERE
    pass
