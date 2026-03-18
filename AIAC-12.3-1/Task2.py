PROMPT:
# Generate a Python program to:
#- Implement Bubble Sort to sort an array.
#- Add inline comments explaining swapping, passes, and termination.
#- Provide time complexity analysis

CODE:
def bubble_sort(arr):
    n = len(arr)
    # Outer loop: runs for each pass
    # After each pass, the largest element moves to the end
    for i in range(n):
        # Inner loop: compares adjacent elements
        for j in range(0, n - i - 1):
            # If current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # Termination: after n-1 passes, array is sorted

data = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", data)
bubble_sort(data)
print("Sorted array:", data)

# -------------------------------
# ⏱️ Time Complexity Analysis:
# Best Case (Already Sorted): O(n)
# Average Case: O(n^2)
# Worst Case (Reverse Sorted): O(n^2)
# Space Complexity: O(1) (in-place sorting)
# -------------------------------

OUTPUT:
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
