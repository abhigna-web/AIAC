PROMPT:
# Generate a Python program to:
# - Store student records (Name, Roll Number, CGPA)
# - Implement Quick Sort and Merge Sort to sort by CGPA (descending)
# - Compare runtime performance for large datasets
# - Display top 10 students

CODE:
import random
import time
class Student:
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa

    def __repr__(self):
        return f"{self.name} ({self.roll}) - CGPA: {self.cgpa}"

# Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2].cgpa
    left = [x for x in arr if x.cgpa > pivot]
    middle = [x for x in arr if x.cgpa == pivot]
    right = [x for x in arr if x.cgpa < pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].cgpa >= right[j].cgpa:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# Function to display top 10 students
def display_top_students(students):
    print("\nTop 10 Students based on CGPA:")
    for i, student in enumerate(students[:10], start=1):
        print(f"{i}. {student}")

# Generate dataset
def generate_students(n):
    students = []
    for i in range(n):
        name = f"Student{i+1}"
        roll = f"R{i+1:03d}"
        cgpa = round(random.uniform(5.0, 10.0), 2)
        students.append(Student(name, roll, cgpa))
    return students

# Main execution
if __name__ == "__main__":
    n = 10000  # Large dataset
    students = generate_students(n)
    # Quick Sort performance
    start = time.time()
    sorted_quick = quick_sort(students)
    quick_time = time.time() - start
    # Merge Sort performance
    start = time.time()
    sorted_merge = merge_sort(students)
    merge_time = time.time() - start
    # Results
    print(f"\nQuick Sort Time: {quick_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    # Display top 10 students (from Quick Sort result)
    display_top_students(sorted_quick)

OUTPUT:
Quick Sort Time: 0.011744 seconds
Merge Sort Time: 0.031107 seconds

Top 10 Students based on CGPA:
1. Student46 (R046) - CGPA: 10.0
2. Student135 (R135) - CGPA: 10.0
3. Student367 (R367) - CGPA: 10.0
4. Student967 (R967) - CGPA: 10.0
5. Student1974 (R1974) - CGPA: 10.0
6. Student2948 (R2948) - CGPA: 10.0
7. Student3400 (R3400) - CGPA: 10.0
8. Student4888 (R4888) - CGPA: 10.0
9. Student4962 (R4962) - CGPA: 10.0
10. Student5490 (R5490) - CGPA: 10.0
