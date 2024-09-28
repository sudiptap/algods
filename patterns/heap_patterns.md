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
