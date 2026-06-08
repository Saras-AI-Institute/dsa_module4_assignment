# Module 4 Lab: High-Frequency Trading (HFT) Analytics Simulator

## Objective
In this lab, you will act as a Performance Engineer optimizing an electronic trading desk. You are tasked with processing blocks of financial transaction records. 

You will directly explore **(Time and Space Complexity)** and **(Performance of Sorting and Searching Algorithms)** by implementing different algorithmic approaches and observing how their execution times diverge as transaction volumes scale from 100 to 10,000+.

---

## System Components to Complete

### Task 1: Sorting Order Books (`sorting_engine.py`)
You must implement five foundational sorting algorithms to sort a list of Transaction IDs or prices:
* **Quadratic Sorts ($O(n^2)$):** Bubble Sort, Selection Sort, and Insertion Sort.
* **Log-Linear Sorts ($O(n \log n)$):** Merge Sort and Quick Sort.

### Task 2: Transaction Auditing (`searching_engine.py`)
You must implement two critical search operations to find a specific transaction value within your ledger:
* **Linear Search ($O(n)$):** Scans unsorted logs sequentially.
* **Binary Search ($O(\log n)$):** Fast divide-and-conquer strategy on pre-sorted ledgers.

---

## Formal Properties Benchmarking
Once your implementations pass the tests, run the following command in your terminal:
```bash
python benchmark_runner.py
