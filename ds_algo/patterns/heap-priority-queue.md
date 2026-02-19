# Heap / Priority Queue

## When to Use
- Need the **k-th largest/smallest** element
- Need to repeatedly get the min or max efficiently
- Merging sorted lists
- Scheduling / interval problems
- Keywords: "k largest", "k smallest", "top k", "median", "merge sorted"

## Core Idea
A heap gives O(log n) insert and O(1) access to min (or max). Python's `heapq` is a **min-heap** by default.

## Templates

### Top K Elements
```python
import heapq

def top_k_largest(nums, k):
    # Min-heap of size k
    return heapq.nlargest(k, nums)

# Manual approach (more flexible):
def top_k(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap  # contains k largest elements
```

### Merge K Sorted Lists
```python
import heapq

def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    return result
```

### Two Heaps (Find Median)
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negate values)
        self.large = []  # min-heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

## Complexity
- Push/Pop: O(log n)
- Peek: O(1)
- Heapify: O(n)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 23 | Merge k Sorted Lists | Hard | Merge K | |
| 215 | Kth Largest Element | Medium | Top K | |
| 253 | Meeting Rooms II | Medium | Min-heap | |
| 295 | Find Median from Data Stream | Hard | Two Heaps | |
| 347 | Top K Frequent Elements | Medium | Top K | |
| 355 | Design Twitter | Medium | Merge K | |
| 373 | Find K Pairs with Smallest Sums | Medium | Top K | |
| 621 | Task Scheduler | Medium | Max-heap | |
| 703 | Kth Largest Element in a Stream | Easy | Top K | |
| 973 | K Closest Points to Origin | Medium | Top K | |

## Tips
- Python `heapq` is min-heap only. For max-heap, negate values
- For "k-th largest", use a min-heap of size k (top of heap = answer)
- Two heaps pattern: max-heap for smaller half, min-heap for larger half
