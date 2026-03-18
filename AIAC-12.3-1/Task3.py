PROMPT:
# Generate a Python program to:
#- Implement Quick Sort and Merge Sort using recursion.
#- Complete missing recursive logic and add docstrings.
#- Compare both algorithms on random, sorted, and reverse-sorted lists.
#- Provide AI-generated explanation of best, average, and worst-case complexities.

CODE:
import random

# Quick Sort Implementation
def quick_sort(arr):
    """
    Quick Sort (Recursive)
    
    Logic:
    - Choose a pivot (here, middle element).
    - Partition array into left (< pivot), middle (= pivot), right (> pivot).
    - Recursively sort left and right partitions.
    
    Time Complexity:
    - Best Case: O(n log n) (balanced partitions)
    - Average Case: O(n log n)
    - Worst Case: O(n^2) (already sorted or reverse sorted with poor pivot choice)
    Space Complexity: O(log n) due to recursion stack.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Merge Sort Implementation
def merge_sort(arr):
    """
    Merge Sort (Recursive)
    
    Logic:
    - Divide array into two halves.
    - Recursively sort each half.
    - Merge sorted halves into one sorted array.
    
    Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n) (always divides evenly)
    Space Complexity: O(n) due to temporary arrays during merging.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    # Merge two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Comparison on Different Inputs
def compare_algorithms():
    sizes = [10, 100]  # dataset sizes for testing
    for n in sizes:
        random_list = [random.randint(1, 1000) for _ in range(n)]
        sorted_list = sorted(random_list)
        reverse_list = sorted(random_list, reverse=True)

        print(f"\nDataset size: {n}")

        # Random list
        print("Random List:")
        print("Quick Sort:", quick_sort(random_list)[:10], "...")  # show first 10
        print("Merge Sort:", merge_sort(random_list)[:10], "...")

        # Sorted list
        print("Sorted List:")
        print("Quick Sort:", quick_sort(sorted_list)[:10], "...")
        print("Merge Sort:", merge_sort(sorted_list)[:10], "...")

        # Reverse sorted list
        print("Reverse Sorted List:")
        print("Quick Sort:", quick_sort(reverse_list)[:10], "...")
        print("Merge Sort:", merge_sort(reverse_list)[:10], "...")


# Run Comparison
if __name__ == "__main__":
    compare_algorithms()

OUTPUT:
Dataset size: 10
Random List:
Quick Sort: [43, 327, 427, 714, 714, 723, 851, 870, 887, 901] ...
Merge Sort: [43, 327, 427, 714, 714, 723, 851, 870, 887, 901] ...
Sorted List:
Quick Sort: [43, 327, 427, 714, 714, 723, 851, 870, 887, 901] ...
Merge Sort: [43, 327, 427, 714, 714, 723, 851, 870, 887, 901] ...
Reverse Sorted List:
Quick Sort: [43, 327, 427, 714, 714, 723, 851, 870, 887, 901] ...
Merge Sort: [43, 327, 427, 714, 714, 723, 851, 870, 887, 901] ...

Dataset size: 100
Random List:
Quick Sort: [29, 30, 37, 39, 47, 48, 55, 56, 60, 84] ...
Merge Sort: [29, 30, 37, 39, 47, 48, 55, 56, 60, 84] ...
Sorted List:
Quick Sort: [29, 30, 37, 39, 47, 48, 55, 56, 60, 84] ...
Merge Sort: [29, 30, 37, 39, 47, 48, 55, 56, 60, 84] ...
Reverse Sorted List:
Quick Sort: [29, 30, 37, 39, 47, 48, 55, 56, 60, 84] ...
Merge Sort: [29, 30, 37, 39, 47, 48, 55, 56, 60, 84] ...
