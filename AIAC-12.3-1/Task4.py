PROMPT:
# Generate a Python program to:
#- Implement efficient search (Binary Search for ID, Hash Map for Name).
#- Implement efficient sort (Quick Sort or Merge Sort) for price/quantity.
#- Compare algorithms with justification in a table.

CODE:
class Product:
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.pid} | {self.name} | Price: {self.price} | Qty: {self.quantity}"

# ---------- Search Algorithms ----------
def binary_search(products, target_id):
    """Binary Search by Product ID (efficient for sorted IDs)."""
    low, high = 0, len(products) - 1
    while low <= high:
        mid = (low + high) // 2
        if products[mid].pid == target_id:
            return products[mid]
        elif products[mid].pid < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

def hashmap_search(products, target_name):
    """Hash Map Search by Product Name (O(1) average)."""
    product_map = {p.name: p for p in products}
    return product_map.get(target_name, None)


# ---------- Sort Algorithms ----------
def quick_sort(arr, key=lambda x: x.price):
    """Quick Sort by given key (price or quantity)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if key(x) < key(pivot)]
    middle = [x for x in arr if key(x) == key(pivot)]
    right = [x for x in arr if key(x) > key(pivot)]
    return quick_sort(left, key) + middle + quick_sort(right, key)

def merge_sort(arr, key=lambda x: x.price):
    """Merge Sort by given key (price or quantity)."""
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------- Example Usage ----------
products = [
    Product(101, "Laptop", 55000, 12),
    Product(102, "Phone", 25000, 30),
    Product(103, "Tablet", 30000, 20),
    Product(104, "Headphones", 2000, 100),
]

# Search
print("Search by ID:", binary_search(sorted(products, key=lambda x: x.pid), 102))
print("Search by Name:", hashmap_search(products, "Tablet"))

# Sort
print("\nSorted by Price (Quick Sort):")
for p in quick_sort(products, key=lambda x: x.price):
    print(p)

print("\nSorted by Quantity (Merge Sort):")
for p in merge_sort(products, key=lambda x: x.quantity):
    print(p)

# ---------- Complexity Table ----------
print("\nOperation → Algorithm → Justification")
print("Search by ID → Binary Search → Efficient O(log n) for sorted IDs")
print("Search by Name → Hash Map → O(1) average lookup, fast for large datasets")
print("Sort by Price/Quantity → Quick Sort/Merge Sort → O(n log n), stable and efficient for thousands of records")

OUTPUT:
Search by ID: 102 | Phone | Price: 25000 | Qty: 30
Search by Name: 103 | Tablet | Price: 30000 | Qty: 20

Sorted by Price (Quick Sort):
104 | Headphones | Price: 2000 | Qty: 100
102 | Phone | Price: 25000 | Qty: 30
103 | Tablet | Price: 30000 | Qty: 20
101 | Laptop | Price: 55000 | Qty: 12

Sorted by Quantity (Merge Sort):
101 | Laptop | Price: 55000 | Qty: 12
103 | Tablet | Price: 30000 | Qty: 20
102 | Phone | Price: 25000 | Qty: 30
104 | Headphones | Price: 2000 | Qty: 100

Operation → Algorithm → Justification
Search by ID → Binary Search → Efficient O(log n) for sorted IDs
Search by Name → Hash Map → O(1) average lookup, fast for large datasets
Sort by Price/Quantity → Quick Sort/Merge Sort → O(n log n), stable and efficient for thousands of records
