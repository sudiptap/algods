## Binary Search Patterns:

### search in sorted array - vanilla binary search

```
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low+high)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            # target is on the left of mid
            high = mid-1
        else:
            low = mid + 1
    return -1 #not found case
```

### find upper/lower bound
#### upper
```
def upper_bound(nums,, target):
    low, high = 0, len(nums)-1
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if target == nums[mid]:
            ans = mid
            # we found one occurrance but we should keep looking to the right 
            low = mid+1
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid-1
    return ans
```
#### lower
```
Similar to upper bound
```
### find first and last position of element in sorted array
```
find lower_bound and upper_bound
```
### find element in rotated sorted array
```
def find(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        # find the sorted half
        if nums[low] <= nums[mid]:
            # check if target falls between low and mid
            if nums[low] <= target < nums[mid] :
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[mid] :
                low = mid + 1
            else:
                high = mid - 1
    return -1
```
#### no duplicate
#### with duplicates
```
def find(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        while low< high and nums[low] == nums[low+1]:
            low += 1
        while low< high and nums[high] == nums[high-1]:
            high-= 1
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        # find the sorted half
        if nums[low] <= nums[mid]:
            # check if target falls between low and mid
            if nums[low] <= target < nums[mid] :
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[mid] :
                low = mid + 1
            else:
                high = mid - 1
    return -1
```
#### find min in rotated sorted array
```
For this problem one should take an example to find the while loop condition and the left and right pointer adjustments. 
```
#### find max in rotated sorted array

#### Single element in sorted array LC-540
```
Idea: if all elements are present with frequency of 2, arr[i] == arr[i+1] if i is even
This rule will not hold beyond seeing a single element with frequency 1.
def singleNonDuplicate(nums):
    low, high = 0, len(nums)-1
    while low<high:
        mid = low + (high-low)//2
        
        # checking if we have even number of elements to the right of mid
        isEven = None 
        if (high-mid)%2 == 0:
            isEven = True
        else:
            isEven = False
        
        if nums[mid] == nums[mid+1]:
            if isEven:
                # element is on the right
                low = mid+2
            else:
                # element must be on the left
                high = mid-1
        else:
            if isEven:
                # element must be on the left
                high = mid # because mid could be the element
            else:
                # element must be on the right
                low = mid+1
        return nums[high]
```
#### kth missing number
```

```

#### Binary search on the ans
minimize max or max min is a pattern for this
```
LC-2439

```
#### Median of two sorted arrays
```
```

## Stack Patterns:

### Monotic stack
#### online stock span - LC 901
```
```

#### 132 Pattern
```
```

#### Remove K Digits
```
Intuition: we should always try to delete digits such that the remaining digits are kept in increasing order
```

### Remving adjacent duplicates
#### Remove all adjacent duplicates - LC 1047
```
```

### Calculator Questions
#### Basic Calculator
```
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        cur = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                cur = cur*10 + int(c)
            elif c in "+-":
                # multiple cur with existing sign and add to res
                res += cur * sign
                cur = 0
                if c == '+':
                    sign = 1
                else:
                    sign = -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                old_sign = stack.pop()
                old_res = stack.pop()
                res += cur * sign
                res *= old_sign
                res += old_res
                cur = 0
        return res + sign*cur
```

### Next smaller to left and right
#### Sum of subarray minimums - LC 907
```
```

### Implement Q using stacks
#### LC 232
```
```

## Queue Patterns:


## LinkedList Patterns:

## Heap Patterns

## Graph Patterns
### basic DFS
```
def hasCycle(graph, curr_node, visited, parent_node):
    visited.add(curr_node)
    for next_node in graph[curr_node]:
        if next_node == parent_node:
            continue
        if next_node in visited:
            return True
        if hasCycle(graph, next_node, visited, curr_node):
            return True
    return False

for curr_node in len(range(nodes)):
    if curr_node not in visited and hasCycle(graph, curr_node, visited, -1):
        return True
return False
```
### basic BFS
```
```
### Cycle detection in undirected graph using DFS
```
def hasCycle(graph, curr_node, visited, in_rec):
    visited.add(curr_node)
    in_rec.add(curr_node)

    for next_node in graph[curr_node]:
        if next_node in visited and hasCycle(graph, next_node, visited, in_rec):
            return True
        else if(next_node in in_rec):
            return True
    
    in_rec.delete(curr_node)
    return False

visited = set()
in_rec = set()
for curr_node in range(len(nodes)):
    if curr_node not in visited and hasCycle(graph, curr_node, visited, in_rec):
        return True
return False
```
### Cycle detection in undirected graph using BFS
```
```
### Topological Sorting using DFS - only in DAGs
```
def dfs(adj, curr_node, vis):
    vis.add(curr_node)
    for next_node in adj[curr_node]:
        if next_node not in vis:
            dfs(adj, next_node, vis)
    stack.add(curr_node)

for curr_node in range(len(nodes)):
    if curr_node not in vis:
        dfs(adj, curr_node, vis)
print(the stack)
```
### Topological Sorting using BFS - only in DAGs, Kahn's Algorithm
```
```
### Disjoint Set - Union Find
```
def find(node, parent):
    if node == parent[node]:
        return node
    
    return find(parent[node], parent)

def union(node_a, node_b, parent):
    par_a = find(node_a, parent)
    par_b = find(node_b, parent)
    if par_a != par_b:
        parent[par_a] = par_b

```
### Disjoint set - Union Find by rank and collapsing find for path compression
```
def find(node, parent):
    if node == parent[node]:
        return node
    
    return parent[node] = find(parent[node], parent)

def union(node_a, node_b, parent, rank):
    par_a = find(node_a, parent)
    par_b = find(node_b, parent)
    if par_a != par_b:
        rank_a = rank[par_a]
        rank_b = rank[par_b]
        if rank_a > rank_b:
            parent[par_b] = par_a
            rank[par_a] += rank[par_b]
        else:
            parent[par_a] = par_b
            rank[par_b] += rank[par_a]
    else:
        return
```
### Disjoint set - Union Find for Cycle detection
```
```
### Dijktra Algorithm
```
```
### Floyed Warshall Algorithm
```
```
### Prims Algorithm for MST
```
```
### Krushkals Algorithm for MST
```
```
### Eular Path
```
```

## Tree Patterns
### Segment Trees
```
def buildTree(curr_index, left, right)
    if left == right:
        segTree[curr_index] = nums[left]
        return
    mid_index = (left+right)//2
    buildTree(2*curr_index+1, left, mid)
    buildTree(2*curr_index+2, mid+1, right)
    segTree[curr_index] = segTree[2*curr_index+1] + segTree[2*curr_index+2] # for sum

```
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