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
