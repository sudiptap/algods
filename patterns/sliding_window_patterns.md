## Sliding Window Patterns
### Pattern 1 - LC 76 Minimum Window Substring
```
```
### Pattern 2 - LC 219
```
```
### Pattern 3 - LC 2444
```
```
### Patern 4 - LC 1493
```
```
### Patter 5 - LC 2024
```
```
### Pattern 6 - Nested double whiles loops
```
```
### Pattern 7 - Monotonic Deque - LC 239
```
step 1: make room for nums[i]
while dq and dq[0]<=i-k:
    dq.pop_left()
step 2: remove all elements smaller than nums[i] since they don't have a chance of being the largest element
while dq and dq[-1]<= nums[i]:
    dq.pop_right()
step 3: put the i-th index inside the dq
    dq.append(i)
step 4: if the window is of length k then add dq[0] to result as we always keep thge biggest element to the front of the dq
    if i>=k-1:
        res.append(dq[0])
```
### Pattern 8 - LC 1838 - revisit
```
```