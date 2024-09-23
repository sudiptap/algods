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

### Level Order Traversal
```
```

### Reconstruction of binary tree
```
LC 105
```

### Lowest Common Ancestor

```
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right
```

### Completeness checking
#### Using BFS
```
Standard BFS with a variable tracking if we have seen null node in past
```
#### Using DFS
```
Represent the binary tree as array where node has index i then left child will have 2i and right child will have 2i+1
if at any point index > total number of nodes then not a complete binary tree
```

### Height of binary tree
```
def getHeight(root):
    if not root:
        return 0

    lefth = getHeight(root.left)
    righth = getHeight(root.right)
    rooth = 1 + max(lefth, righth)
    return rooth 
```
#### Remove from leaves periodically
```
Use the above logic to calculate height, as you get rooth at every step put it as key in a map and value would be the node
```

### Binary Tree Pruning
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return None
        
        root.left = self.helper(root.left)
        root.right =self.helper(root.right)

        if not root.left and not root.right and root.val == 0:
            return None
        else:
            return root

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root)
```
### Path Sum Pattern
```
LC113
LC112
```

### Complete tree pattern
```
LC222
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
class Solution:
    def getLeftExtremeDepth(self, root):
        if not root:
            return 0
        
        return 1 + self.getLeftExtremeDepth(root.left)
    
    def getRightExtremeDepth(self, root):
        if not root:
            return 0
        
        return 1 + self.getRightExtremeDepth(root.right)
    
    
    def helper(self, root):
        if not root:
            return 0
        
        leftExtremeDepth = self.getLeftExtremeDepth(root)
        rightExtremeDepth = self.getRightExtremeDepth(root)
        
        if leftExtremeDepth == rightExtremeDepth:
            return 2 ** leftExtremeDepth - 1
        else:
            return 1 + self.helper(root.left) + self.helper(root.right) 
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)
"""
class Solution:
    
    def getLeftExtremeDepth(self, root):
        if not root:
            return 0
        return 1 + self.getLeftExtremeDepth(root.left)
    
    def getRightExtremeDepth(self, root):
        if not root:
            return 0
        return 1 + self.getRightExtremeDepth(root.right)
    
    def helper(self, root):
        if not root:
            return 0
        
        leftExtremeDepth = self.getLeftExtremeDepth(root)
        rightExtremeDepth = self.getRightExtremeDepth(root)
        
        if leftExtremeDepth == rightExtremeDepth:
            return 2 ** leftExtremeDepth - 1
        else:
            return self.helper(root.left) + self.helper(root.right) + 1
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)
        
```
### Splitting Tree Sum - LC1339
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        self.maxP = 0

    def getTreeSum(self, root):
        if not root:
            return 0
        
        leftSum = self.getTreeSum(root.left)
        rightSum = self.getTreeSum(root.right)
        treeSum = root.val + leftSum + rightSum

        return treeSum

    def find(self, root):
        if not root:
            return 0
        
        # post order
        leftSum = self.find(root.left)
        rightSum = self.find(root.right)
        treeSum = root.val + leftSum + rightSum
        reaminingSum = (self.sum - treeSum)
        self.maxP = max(self.maxP, reaminingSum*treeSum)
        return treeSum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.sum = self.getTreeSum(root)
        self.find(root)
        return self.maxP % (10**9 + 7)

        
```
### Maximum Path Sum
```
LC124
Idea: If I am standing at a node i in the tree
There are the following posibilities
1. left subtree of node i , node i and right subtree of node i builds the path - in this case we found the best path so far
2. left subtree of node i and node i builds the path - in this case, we can still keeop building the path upward to the ancestors of node i
3. right subtree of node i and node i builds the path - in this case, we can still keeop building the path upward to the ancestors of node i
4. only node i builds the path - here too, taking left and/or right subtree reduces the path sum, hence only root is better but we could extend the path upward too.
We should not return case 1 since the path is already found, but the max of case2,3,4 since there is still possibility of path building upward node i

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pathSum = 0
    
    def helper(self, root):
        if not root:
            return 0
        
        leftSum = self.helper(root.left)
        rightSum = self.helper(root.right)

        path_left_root_right = leftSum + root.val + rightSum
        path_left_root = leftSum + root.val
        path_right_root = rightSum + root.val
        path_only_root = root.val

        self.pathSum = max(
            self.pathSum,
            path_left_root_right,
            path_left_root,
            path_right_root,
            path_only_root
        )

        return max(path_left_root, path_right_root, path_only_root)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.pathSum

```
### Root to leaf sum number
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, curr):
        curr = curr*10 + root.val
        if not root.left and not root.right:
            return curr
        l = self.helper(root.left, curr)
        r = self.helper(root.right, curr)

        return l+r

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
```

### Construct BT from Inorder and PostOrder traversal
```
```

### Longest ZigZag Path in a Binary Tree - LC1372
```
If I am at a node called root, I will pass my left child a message to goRight and right child a message to goLeft, if goLeft if True and I am going left then steps = steps+1, else steps = 1, viceversa, at each step update maxPath = max(maxPath, steps)
```

### Maximum Width of BT - LC662
```
Pattern is to use the following : if a node has index i, left child would have index 2i+1 and right child 2i+2 . Then use BFS to level order traverse the tree
```

### All Nodes Distance K in Binary Tree - LC863
```
e.g. LC2385
Get map to store parent pointer, then perform level order traversal

```

### Validate binary tree nodes - LC1361
```
```
### Find Largest value in each Tree row - LC515
```
BFS level order solution is easy
DFS pattern is interesting
idea is the following
1. traverse the tree in inorder fashion
2. child_i will be called with depth(node i) + 1, root node being at depth 0
3. each time a node is visited add the node to a map,where map[depth] = node_val, here if the len(map)== depth then, I am visiting this depth for the first time and hence we will do map[depth] = node_val, however if len(map) > depth then, we have visited this depth befiore so map[depth] = max(map[depth], node_val)
```

### Amount of time binary tree could be infected - LC2385
```
```

### Distribute Coins in BT - LC979
```
```

### Count the nodes at distance K from leaf
```
```

### Diameter of a BT - LC543
```
Very standard pattern where we do the following
standing at a node we find current value might be the asnwer, but there is a possibility that the best answer will be found by extending the solution upward
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    
    def helper(self, root):
        if not root:
            return 0
        
        lh, rh = self.helper(root.left), self.helper(root.right)
        self.diameter = max(self.diameter, lh+rh)

        return max(lh, rh) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.diameter
```

### Morriss Traversal
```
```


















































## Practice
LC105
LC958
LC113
LC112
LC1339
LC1361 - validate binary tree nodes
LC2385 - do using DFS