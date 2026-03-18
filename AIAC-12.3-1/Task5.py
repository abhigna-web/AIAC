PROMPT:
Generate a Python program:
- Simulate stock data (symbol, opening price, closing price).
- Implement Heap Sort to rank stocks by percentage change.
- Implement Hash Map search for stock symbol lookup.
- Compare performance with sorted() and dict lookups.
- Provide trade-off analysis in comments.

CODE:
import random
import time
import heapq

# Simulate Stock Data

class Stock:
    def __init__(self, symbol, opening, closing):
        self.symbol = symbol
        self.opening = opening
        self.closing = closing
        self.change = ((closing - opening) / opening) * 100  # % change

    def __repr__(self):
        return f"{self.symbol} | Open: {self.opening} | Close: {self.closing} | Change: {self.change:.2f}%"

def generate_stocks(n=10):
    stocks = []
    for i in range(n):
        symbol = f"STK{i+1}"
        opening = round(random.uniform(100, 500), 2)
        closing = round(opening * random.uniform(0.9, 1.1), 2)  # simulate ±10% change
        stocks.append(Stock(symbol, opening, closing))
    return stocks

# Heap Sort by % Change
def heap_sort(stocks):
    """Heap Sort using heapq to rank stocks by percentage change."""
    heap = [(-s.change, s) for s in stocks]  # negative for max-heap
    heapq.heapify(heap)
    sorted_stocks = []
    while heap:
        sorted_stocks.append(heapq.heappop(heap)[1])
    return sorted_stocks


# Hash Map Search
def hashmap_search(stocks, target_symbol):
    """Hash Map search for O(1) average lookup."""
    stock_map = {s.symbol: s for s in stocks}
    return stock_map.get(target_symbol, None)

# Performance Comparison
def compare_performance(stocks):
    # Heap Sort
    start = time.time()
    sorted_heap = heap_sort(stocks)
    heap_time = time.time() - start

    # Built-in sorted()
    start = time.time()
    sorted_builtin = sorted(stocks, key=lambda s: s.change, reverse=True)
    builtin_time = time.time() - start

    # Hash Map Search
    start = time.time()
    result_hash = hashmap_search(stocks, stocks[0].symbol)
    hash_time = time.time() - start

    # Dict Lookup (same as hash map)
    stock_dict = {s.symbol: s for s in stocks}
    start = time.time()
    result_dict = stock_dict.get(stocks[0].symbol)
    dict_time = time.time() - start

    print("\n--- Performance Comparison ---")
    print(f"Heap Sort Time: {heap_time:.6f} seconds")
    print(f"Built-in sorted() Time: {builtin_time:.6f} seconds")
    print(f"Hash Map Search Time: {hash_time:.6f} seconds")
    print(f"Dict Lookup Time: {dict_time:.6f} seconds")

    print("\nTop 5 Stocks by % Change (Heap Sort):")
    for s in sorted_heap[:5]:
        print(s)

# Run Example
if __name__ == "__main__":
    stocks = generate_stocks(15)
    print("Original Stock Data:")
    for s in stocks:
        print(s)

    # Search Example
    print("\nSearch by Symbol (Hash Map):")
    print(hashmap_search(stocks, "STK5"))

    # Compare Performance
    compare_performance(stocks)

# Trade-off Analysis (in comments):
# Heap Sort: O(n log n), efficient for large datasets, but Python's built-in sorted() is highly optimized in C.
# Hash Map Search: O(1) average, ideal for instant lookups.
# Built-in sorted(): O(n log n), faster in practice due to optimizations.
# Dict Lookup: Same as hash map, O(1).
# Trade-off: For real-time stock analysis, built-in sorted() and dict lookups are usually faster,
# but Heap Sort and explicit hash maps demonstrate algorithmic efficiency and control.

OUTPUT:
Original Stock Data:
STK1 | Open: 172.02 | Close: 187.74 | Change: 9.14%
STK2 | Open: 321.26 | Close: 352.52 | Change: 9.73%
STK3 | Open: 467.14 | Close: 443.05 | Change: -5.16%
STK4 | Open: 357.98 | Close: 340.44 | Change: -4.90%
STK5 | Open: 184.41 | Close: 193.29 | Change: 4.82%
STK6 | Open: 236.59 | Close: 239.37 | Change: 1.18%
STK7 | Open: 270.61 | Close: 249.88 | Change: -7.66%
STK8 | Open: 203.13 | Close: 195.75 | Change: -3.63%
STK9 | Open: 252.63 | Close: 265.02 | Change: 4.90%
STK10 | Open: 271.88 | Close: 266.08 | Change: -2.13%
STK11 | Open: 338.24 | Close: 360.6 | Change: 6.61%
STK12 | Open: 480.16 | Close: 461.64 | Change: -3.86%
STK13 | Open: 158.78 | Close: 169.5 | Change: 6.75%
STK14 | Open: 124.13 | Close: 133.84 | Change: 7.82%
STK15 | Open: 123.08 | Close: 117.89 | Change: -4.22%

Search by Symbol (Hash Map):
STK5 | Open: 184.41 | Close: 193.29 | Change: 4.82%

--- Performance Comparison ---
Heap Sort Time: 0.000019 seconds
Built-in sorted() Time: 0.000016 seconds
Hash Map Search Time: 0.000004 seconds
Dict Lookup Time: 0.000000 seconds


Explanation:
We built a small stock analysis tool. First, we simulate stock data with a symbol, opening price, and closing price, 
then calculate the percentage change. To rank stocks by gain/loss, we used Heap Sort because it’s efficient (𝑂(𝑛log𝑛)) 
and good for large datasets. For searching by symbol, we used a Hash Map (Python dictionary) since it gives almost instant lookups (𝑂(1) average time).

We also compared our algorithms with Python’s built‑in sorted() and direct dict lookups. The built‑in functions are faster in practice because they’re optimized in C,
but using Heap Sort and Hash Maps shows the algorithmic logic clearly.
