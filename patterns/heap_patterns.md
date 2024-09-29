### Find Median from data stream
LC 295
```
Use two heaps, left_max_heap and right_min_heap, as values arrive check if it is bigger than the top of left_max_heap, if so, push it to right_min_heap else to left_max_heap. CHeck if the len(left_max_heap) - len(right_min_heap) is more than 1, if so, pop from left_max_heap and push to right_min_heap. Check if the len(right_min_heap) - len(left_max_heap) is more than 1, if so, pop from right_min_heap and push to left_max_heap.
At any point to calculate median, check the size of heaps, if equal, return (left_max_heap.top() + right_min_heap.top()) / 2, else return left_max_heap.top() if left_max_heap has more elements.
```

### Merge k sorted lists
LC 23
```
```
### Remove Stones to Minimize the Total
LC 1962
```
Use a max heap to keep track of the stones, and pop the two largest stones and push the difference back into the heap. Repeat until the heap has less than 2 stones. Return the sum of the stones.
```
### Single Threaded CPU
LC 1834
```
Use a min heap to keep track of the tasks, and a max heap to keep track of the tasks that are available to be executed. The min heap will store the tasks in order of their enqueue time, and the max heap will store the tasks in order of their processing time. If two tasks have the same processing time, then we can use the id to sort them.

class TaskHeap:
    def __init__(self, task_idx, enq_time, duration):
        self.task_idx = task_idx
        self.enq_time = enq_time
        self.duration = duration

    def __lt__(self, other):
        if self.duration == other.duration:
            return self.task_idx < other.task_idx
        else:
            return self.duration < other.duration

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = []
        for idx, task in enumerate(tasks):
            sorted_tasks.append([idx, task[0], task[1]])
        sorted_tasks.sort(key = lambda task: task[1])
        pq = []
        task_idx, ctime = 0, 0
        res = []
        while task_idx < len(sorted_tasks) or pq:
            if not pq and ctime < sorted_tasks[task_idx][1]:
                ctime = sorted_tasks[task_idx][1]
            while task_idx < len(sorted_tasks) and sorted_tasks[task_idx][1] <= ctime:
                heapq.heappush(pq, TaskHeap(sorted_tasks[task_idx][0], sorted_tasks[task_idx][1], sorted_tasks[task_idx][2]))
                task_idx += 1
            # pop from the pq
            top = heapq.heappop(pq)
            ctime += top.duration
            res.append(top.task_idx)
        return res
```

### Maximum Subsequence Score
```
Leetcode-2542
revisit
```

### Total Cost to Hire K Workers
```
LC 2462
```

### Find K Pairs with Smallest Sums
```
LC 373
```

### Task Scheduler
```
LC 621
class HeapNode:
    def __init__(self, task, freq):
        self.task = task
        self.freq = freq
        
    def __gt__(self, other):
        return self.freq < other.freq
    
    def __repr__(self):
        return f"task = {self.task}, freq = {self.freq}"

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = dict()
        total_tasks = 0
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1
            total_tasks += 1
        # print(f"freq = {freq}, total_tasks = {total_tasks}")
        
        heap = []
        heapq.heapify(heap)
        
        for task, task_freq in freq.items():
            heapq.heappush(heap, HeapNode(task, task_freq))
        
        completed = 0
        ans = 0
        
        while len(heap) > 0:
            
            buffer = []
            for i in range(n+1):
                if len(heap) > 0:
                    top = heapq.heappop(heap)
                    buffer.append(top)
            for entry in buffer:
                #print(f"entry = {entry}")
                if entry.freq - 1 > 0:
                    heapq.heappush(heap, HeapNode(entry.task, entry.freq - 1))
            ans += len(buffer) if len(heap) == 0 else (n+1)
            #print(f"ans = {ans}")
        return ans
            
            
                
            
        
        
```

### IPO
```
LC 502

```