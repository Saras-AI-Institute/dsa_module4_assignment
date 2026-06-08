```python
"""
Module 4: Sorting Engine Optimization
Implement all five algorithms to sort lists of integers/floats in ascending order.
Do NOT use Python's built-in .sort() or sorted().
"""

# =========================================================================
# QUADRATIC SORTING ALGORITHMS O(n^2)
# =========================================================================

def bubble_sort(arr: list) -> list:
    """
    TODO: Implement Bubble Sort.
    Iteratively step through the list, compare adjacent elements, and swap them.
    """
    # YOUR CODE HERE
    pass

def selection_sort(arr: list) -> list:
    """
    TODO: Implement Selection Sort.
    Maintain a sorted boundary and repeatedly find the minimum element 
    from the unsorted section to swap it to the front.
    """
    # YOUR CODE HERE
    pass

def insertion_sort(arr: list) -> list:
    ```
    TODO: Implement Insertion Sort.
    Build the final sorted list one item at a time by consuming one input 
    element per repetition and inserting it into its correct relative spot.
    ```
    # YOUR CODE HERE
    pass

# =========================================================================
# LOG-LINEAR SORTING ALGORITHMS O(n log n)
# =========================================================================

def merge_sort(arr: list) -> list:
    """
    TODO: Implement Merge Sort (Divide and Conquer).
    Recursively split the array in half, sort the halves, and merge them back together.
    Returns a new sorted list.
    """
    # YOUR CODE HERE
    pass

def quick_sort(arr: list) -> list:
    """
    TODO: Implement Quick Sort.
    Pick a pivot element, partition the remaining elements into sub-arrays 
    of smaller and larger values, and recursively sort the sub-arrays.
    """
    # YOUR CODE HERE
    pass
