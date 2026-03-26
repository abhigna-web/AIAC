#TASK1
#Generate a Python class named Stack with the following methods:
#- push(item): adds an element to the stack
#- pop(): removes and returns the top element of the stack
#- peek(): returns the top element without removing it
#- is_empty(): returns True if the stack is empty, otherwise False
#Include proper docstrings for each method.
class Stack:
    # Constructor: initializes an empty list to store stack items
    def __init__(self):
        self.items = []
    # Push: add an item to the top of the stack
    def push(self, item):
        self.items.append(item)
    # Pop: remove and return the top item
    # Raises error if stack is empty
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    # Peek: return the top item without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    # is_empty: check if stack has no elements
    def is_empty(self):
        return len(self.items) == 0
    # size: return number of elements in stack
    def size(self):
        return len(self.items)
    # __str__: string representation for easy printing
    def __str__(self):
        return "Stack: " + str(self.items)
stack = Stack()        # create empty stack
stack.push(10)         # add 10
stack.push(20)         # add 20
stack.push(30)         # add 30
print(stack)           # Stack: [10, 20, 30]
print(stack.peek())    # 30 (top element)
print(stack.pop())     # removes and returns 30
print(stack.is_empty())# False (still has items)
print(stack.size())    # 2 (two items left)



#TASK 2
#Generate a Python Queue class using lists with enqueue, dequeue, peek, and size methods. Add short comments for explanation.
class Queue:
    # Constructor: initializes an empty list
    def __init__(self):
        self.items = []
    # Enqueue: add item to the end
    def enqueue(self, item):
        self.items.append(item)
    # Dequeue: remove and return front item
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
    # Peek: return front item without removing
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]
    # Check if queue is empty
    def is_empty(self):
        return len(self.items) == 0
    # Return number of items
    def size(self):
        return len(self.items)
    # String representation for printing
    def __str__(self):
        return "Queue: " + str(self.items)
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue)           # Queue: [10, 20, 30]
print(queue.peek())    
print(queue.dequeue()) 
print(queue.is_empty())
print(queue.size())    



#TASK 3
#Generate a Python Singly Linked List with Node and LinkedList classes. Include insert and display methods with comments.
# Node class: represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None   
# LinkedList class: manages nodes
class LinkedList:
    def __init__(self):
        self.head = None   # start of the list
    # Insert: add new node at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:   # if list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next: # traverse to last node
                current = current.next
            current.next = new_node
    # Display: print all nodes
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
#Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()



#TASK 4
#Generate a Python Binary Search Tree (BST) class with recursive insert and in-order traversal methods.
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None   
        self.right = None  
# BST class: manages the tree
class BST:
    def __init__(self):
        self.root = None   # start with empty tree
    # Insert: recursive helper
    def _insert(self, root, data):
        if root is None:   # if empty spot found
            return Node(data)
        if data < root.data:   # go left
            root.left = self._insert(root.left, data)
        else:                  # go right
            root.right = self._insert(root.right, data)
        return root
    # Public insert method
    def insert(self, data):
        self.root = self._insert(self.root, data)
    # In-order traversal: left → root → right
    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.data, end=" ")
            self._inorder(root.right)
    # Public traversal method
    def inorder(self):
        self._inorder(self.root)
        print()
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
bst.inorder()



#TASK 5
#Generate a Python HashTable class using lists with insert, search, and delete methods. Handle collisions using chaining.
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of buckets
    # Hash function: maps key to index
    def _hash(self, key):
        return hash(key) % self.size
    # Insert: add key-value pair
    def insert(self, key, value):
        index = self._hash(key)
        # check if key already exists → update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # otherwise add new pair
        self.table[index].append([key, value])
    # Search: find value by key
    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # not found
    # Delete: remove key-value pair
    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False  
    # Display: show hash table contents
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
ht = HashTable()
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("grape", 300)
print(ht.search("banana"))  # 200
ht.delete("apple")
ht.display()



#TASK 6
#Generate a Python Graph class using an adjacency list with methods to add vertices, add edges, and display connections. Add short comments.
# Graph implementation using adjacency list
class Graph:
    def __init__(self):
        self.adj_list = {}  # dictionary to store vertices and edges
    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    # Add an edge (connection) between two vertices
    def add_edge(self, v1, v2):
        # ensure both vertices exist
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        # add connection (undirected graph)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
    # Display all connections
    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.display()



#TASK 7
#Generate a python implementation with enqueue(priority),dequeue(highest priority),and display methods.
import heapq
# Priority Queue using heapq (min-heap)
class PriorityQueue:
    def __init__(self):
        self.queue = []  # list to store heap
    # Enqueue: add item with priority
    def enqueue(self, priority, item):
        heapq.heappush(self.queue, (priority, item))
    # Dequeue: remove and return item with smallest priority
    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)
        return None
    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    # Display: show all elements in heap order
    def display(self):
        print("Priority Queue:", self.queue)
pq = PriorityQueue()
pq.enqueue(2, "task B")
pq.enqueue(1, "task A")
pq.enqueue(3, "task C")
pq.display()
print(pq.dequeue())
pq.display()



#TASK 8
#Generate a Python DequeDS class using collections.deque with insert and remove from both ends, plus display method. Add docstrings.
from collections import deque
class DequeDS:
    """
    Double-ended queue (Deque) implementation using collections.deque.
    Supports insertion and removal from both ends.
    """
    def __init__(self):
        """Initialize an empty deque."""
        self.deque = deque()

    def insert_front(self, item):
        """Insert an item at the front of the deque."""
        self.deque.appendleft(item)

    def insert_rear(self, item):
        """Insert an item at the rear of the deque."""
        self.deque.append(item)

    def remove_front(self):
        """Remove and return the front item of the deque."""
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        return self.deque.popleft()

    def remove_rear(self):
        """Remove and return the rear item of the deque."""
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        return self.deque.pop()

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.deque) == 0

    def display(self):
        """Display the contents of the deque."""
        print("Deque:", list(self.deque))
dq = DequeDS()
dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(5)
dq.display()            
print(dq.remove_front())
print(dq.remove_rear()) 
dq.display()



#TASK 9
#Generate a Python Queue class for campus resource management system that handles student attendance,event registration system,library book borrowing,bus scheduling system and cafeteria order queue with data stucture from stack,queue,priority queue,linked list,binary search tree(BST),graph,hash table and deque.
class CampusQueue:
    """
    Queue class for managing various campus resources such as student attendance,
    event registration, library book borrowing, bus scheduling, and cafeteria orders.
    """
    def __init__(self):
        self.attendance_queue = []  # Queue for student attendance
        self.event_registration_queue = []  # Queue for event registration
        self.library_borrowing_queue = []  # Queue for library book borrowing
        self.bus_scheduling_queue = []  # Queue for bus scheduling
        self.cafeteria_order_queue = []  # Queue for cafeteria orders

    def enqueue_attendance(self, student_id):
        """Add a student to the attendance queue."""
        self.attendance_queue.append(student_id)

    def dequeue_attendance(self):
        """Remove and return the next student in the attendance queue."""
        if not self.attendance_queue:
            raise IndexError("Attendance queue is empty")
        return self.attendance_queue.pop(0)

    def enqueue_event_registration(self, event_name):
        """Add an event to the registration queue."""
        self.event_registration_queue.append(event_name)

    def dequeue_event_registration(self):
        """Remove and return the next event in the registration queue."""
        if not self.event_registration_queue:
            raise IndexError("Event registration queue is empty")
        return self.event_registration_queue.pop(0)

    def enqueue_library_borrowing(self, book_title):
        """Add a book to the borrowing queue."""
        self.library_borrowing_queue.append(book_title)

    def dequeue_library_borrowing(self):
        """Remove and return the next book in the borrowing queue."""
        if not self.library_borrowing_queue:
            raise IndexError("Library borrowing queue is empty")
        return self.library_borrowing_queue.pop(0)

    def enqueue_bus_scheduling(self, bus_route):
        """Add a bus route to the scheduling queue."""
        self.bus_scheduling_queue.append(bus_route)

    def dequeue_bus_scheduling(self):
        """Remove and return the next bus route in the scheduling queue."""
        if not self.bus_scheduling_queue:
            raise IndexError("Bus scheduling queue is empty")
        return self.bus_scheduling_queue.pop(0)

    def enqueue_cafeteria_order(self, order_details):
        """Add an order to the cafeteria order queue."""
        self.cafeteria_order_queue.append(order_details)

    def dequeue_cafeteria_order(self):
        """Remove and return the next order in the cafeteria order queue."""
        if not self.cafeteria_order_queue:
            raise IndexError("Cafeteria order queue is empty")
        return self.cafeteria_order_queue.pop(0)
# Example usage
campus_queue = CampusQueue()
campus_queue.enqueue_attendance("Student A")
campus_queue.enqueue_attendance("Student B")
print(campus_queue.dequeue_attendance())  # Student A
campus_queue.enqueue_event_registration("Event 1")
print(campus_queue.dequeue_event_registration())  # Event 1
campus_queue.enqueue_library_borrowing("Book 1")
print(campus_queue.dequeue_library_borrowing())  # Book 1
campus_queue.enqueue_bus_scheduling("Route 1")
print(campus_queue.dequeue_bus_scheduling())  # Route 1
campus_queue.enqueue_cafeteria_order("Order 1")
print(campus_queue.dequeue_cafeteria_order())  # Order 1



#TASK 10
#Generate a table mapping each e-commerce feature to the most appropriate data structure (from Stack, Queue, Priority Queue, Linked List, BST, Graph, Hash Table, Deque) with 2–3 sentence justification. Then implement one selected feature as a working Python program with comments and docstrings.
'''| E-commerce Feature       | Data Structure     | Justification                                                                 |
|-------------------------|--------------------|-------------------------------------------------------------------------------|
| Product Catalog         | Hash Table         | A hash table allows for fast lookups of products by their unique identifiers, making it ideal for managing a large product catalog. It also handles collisions efficiently, which is important when multiple products may have similar attributes. |
| Shopping Cart           | Linked List        | A linked list is suitable for a shopping cart because it allows for dynamic resizing as items are added or removed. It also provides efficient insertion and deletion operations, which are common in a shopping cart scenario. |
| Order Processing        | Queue              | A queue is ideal for order processing as it follows the First-In-First-Out (FIFO) principle, ensuring that orders are processed in the order they were received. This helps maintain fairness and efficiency in handling customer orders. |'''
# Implementing the Order Processing feature using a Queue
class Queue:
    """
    Simple FIFO Queue for order processing in e-commerce.
    """

    def __init__(self):
        self.items = []  # list to store orders

    def enqueue(self, order):
        """Add an order to the end of the queue."""
        self.items.append(order)

    def dequeue(self):
        """Remove and return the first order."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the first order without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def display(self):
        """Display all current orders in the queue."""
        print("Orders in Queue:", self.items)
orders = Queue()
orders.enqueue("Order #101: Laptop")
orders.enqueue("Order #102: Phone")
orders.enqueue("Order #103: Headphones")
orders.display()            # Orders in Queue: ['Order #101: Laptop', 'Order #102: Phone', 'Order #103: Headphones']
print(orders.dequeue())     # Order #101: Laptop
print(orders.peek())        # Order #102: Phone
orders.display()            # Orders in Queue: ['Order #102: Phone', 'Order #103: Headphones']
