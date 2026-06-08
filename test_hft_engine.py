import pytest
import random
from sorting_engine import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from searching_engine import linear_search, binary_search

@pytest.fixture
def sample_data():
    return [42, 12, 89, 23, 11, 45, 7]

@pytest.fixture
def sorted_sample_data():
    return [7, 11, 12, 23, 42, 45, 89]

@pytest.mark.parametrize("sort_func", [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort])
def test_all_sorting_algorithms(sort_func, sample_data, sorted_sample_data):
    res = sort_func(sample_data.copy())
    # Handle both in-place modifications and copy returns safely
    actual_sorted = res if res is not None else sample_data
    assert actual_sorted == sorted_sample_data, f"Failed using {sort_func.__name__}"

def test_searching_algorithms(sorted_sample_data):
    # Test found states
    assert linear_search(sorted_sample_data, 23) == 3
    assert binary_search(sorted_sample_data, 23) == 3
    
    # Test missing states
    assert linear_search(sorted_sample_data, 99) == -1
    assert binary_search(sorted_sample_data, 99) == -1
