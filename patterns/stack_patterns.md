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
LC 224
I
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

LC 227
II
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        op = "+"
        prev = cur = 0
        i = 0
        while i< len(s):
            ch = s[i]
            # check if ch is a digit
            if ch.isdigit():
                num = 0
                while i< len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                i -= 1
                if op == "+":
                    res += num
                    prev = num
                elif op == "-":
                    res -= num
                    prev = -num
                elif op == "*":
                    res -= prev
                    res += prev * num
                    prev = prev * num
                elif op == "/":
                    res -= prev
                    res += int(prev / num)
                    prev = int(prev / num)
            elif ch != " ":
                op = ch
            i += 1
        return res
```

### Next smaller to left and right
#### Sum of subarray minimums - LC 907
```
```

### Implement Q using stacks
#### LC 232
```
```

### LC 426
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        head = tail = None

        def inorder(root):
            nonlocal head, tail
            if not root:
                return
            
            inorder(root.left)

            if not tail:
                head = root
            else:
                tail.right = root
                root.left = tail
            tail = root

            inorder(root.right)
        
        inorder(root)
        tail.right = head
        head.left =tail

        

        return head


# class Solution:
#     def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if not root:
#             return None
#         head = tail = None
#         def inorder(node):
#             nonlocal head, tail
#             if not node:
#                 return
            
#             inorder(node.left)
            
#             if head:
#                 tail.right = node
#                 node.left = tail
#             else:
#                 head = node
#             tail = node
            
#             inorder(node.right)
        
        
        
#         inorder(root)
        
#         head.left = tail
#         tail.right = head
        
#         return head
```

### 921. Minimum Add to Make Parentheses Valid - constant space solution
```
declare openp and closep, if ch == "(" then openp += 1, if ch == ")" and if openp > 0 then openp -= 1, else closep += 1, return openp + closep
```

### 636. Exclusive Time of Functions
```
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        if not logs or len(logs) == 0:
            return res
        firstRec = logs[0].split(":")
        id, action, ts = int(firstRec[0]), firstRec[1], int(firstRec[2])
        stack.append(id)
        prev_ts = ts
        for i in range(1, len(logs)):
            id, action, ts = logs[i].split(":")
            id = int(id)
            ts = int(ts)
            if action == "start":
                if stack:
                    prev_id = stack[-1]
                res[prev_id] += ts - prev_ts
                stack.append(id)
                prev_ts = ts
            else:
                prev_id = stack[-1]
                res[prev_id] += ts - prev_ts + 1
                stack.pop()
                prev_ts = ts + 1
        return res
```

### LC 536 Construct BT from string
```
https://www.youtube.com/watch?v=AY7ZO0Q1s0k
idea: use a stack, build the number and push, if you see a open paren, then push, close paren then pop, do a dry run

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        #base condition
        if not s or len(s) == 0:
            return None
        stack = []
        i = 0
        while i< len(s):
            ch = s[i]
            if ch == '-':
                # we are expecting a number
                i += 1
                num = 0
                while i< len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
                stack.append(TreeNode(-num))
            elif ch.isdigit():
                num = 0
                while i< len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
                stack.append(TreeNode(num))
            elif ch == ")":
                popped = stack.pop()
                parent = stack[-1]
                if parent.left == None:
                    parent.left = (popped)
                else:
                    parent.right = (popped)
            i += 1
        return stack[0]


```