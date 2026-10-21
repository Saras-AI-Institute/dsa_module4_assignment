"""
Module 4: Searching Engine Validation
Implement linear and binary search algorithms.
"""

def linear_search(arr: list, target: any) -> int:
    """
    TODO: Implement Linear Search.
    1. Loop through the list using a standard `for i in range(len(arr))` or `enumerate(arr)`.
    2. If arr[i] == target, return index `i`.
    3. If the loop finishes without finding the target, return -1.
    """
    # YOUR CODE HERE
    pass

def binary_search(sorted_arr: list, target: any) -> int:
    """
    TODO: Implement Binary Search.
    1. Set pointers: left = 0, right = len(sorted_arr) - 1.
    2. While left <= right:
       - Find mid = (left + right) // 2
       - If sorted_arr[mid] == target, return mid.
       - Else if sorted_arr[mid] < target, move left boundary (left = mid + 1).
       - Else, move right boundary (right = mid - 1).
    3. Return -1 if not found.
    """
    # YOUR CODE HERE
    pass
