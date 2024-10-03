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

LC 772
Basic Calculator III
class Solution:
    def calculate(self, s: str) -> int:
        stack, sign, num = [], '+', 0
        for i, c in enumerate(s + '+'):
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            elif c == '(':
                stack.append(sign)
                stack.append('(')
                sign = '+'
            elif c in '+-*/)':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                if c == ')':
                    num, item = 0, stack.pop()
                    while item != '(':
                        num += item
                        item = stack.pop()
                    sign = stack.pop()
                else:
                    sign, num = c, 0
        return sum(stack)
        
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

### LC 1047 - Remove all adjacent duplicates in a string
```
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for idx in range(len(s)):
            if not stack or s[stack[-1]] != s[idx]:
                stack.append(idx)
            else:
                while stack and s[stack[-1]] == s[idx]:
                    stack.pop()
        return "".join(s[c] for c in stack)

LC 1209

```

### 1541. Minimum Insertions to Balance a Parentheses String
```
class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        s = s.replace('))', '}')
        open_bracket_count = 0

        for c in s:
            if c == '(':
                open_bracket_count += 1
                
            else:
			
                # For ) you need to add 1 char to get ))
                if c == ')': 
                    count += 1

                # Matching ( for ) or ))
                if open_bracket_count:
                    open_bracket_count -= 1


                # No Matching ( for ) or ))
                # Need to insert ( to balance string
                else:
                    count += 1

        return count + open_bracket_count * 2
```

### 20. Valid Parentheses
```
need a stack, ([)] is invalid
```

### LC 114 Flatten BT to LL
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def helper(root):
            nonlocal prev
            if not root:
                return
            
            helper(root.right)
            helper(root.left)

            root.right = prev
            root.left = None
            prev = root
        
        helper(root)
```

### LC 234 - Palindrome LL
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # use slow and fast pointers to find the middle
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow is pointing the mid node

        # reverse the second half of the linkedlist
        prev, cur = None, slow
        while cur:
            # hold the next pointer to cur
            nxt = cur.next
            # reverse the node pointers
            cur.next = prev
            # advance the prv
            prev = cur
            # adavcne the cur
            cur = nxt
        # prev will be pointing the first node of second half

        # check for palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
```

### LC 1944 - Number of visible people in a q
```
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and heights[i] > st[-1]:
                st.pop()
                ans[i] += 1
            if st:
                ans[i] += 1
            st.append(heights[i])
        return ans
```

### LC 42 - Trapping rain water
```
class Solution:
    
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxl, maxr = height[l], height[r]
        res = 0

        while l < r:
            if maxl <= maxr:
                l += 1
                res += max((maxl - height[l]), 0)
                maxl = max(maxl, height[l])
            else:
                r -= 1
                res += max((maxr - height[r]), 0)
                maxr = max(maxr, height[r])
        return res
```

### LC 2281
```
very hard
```

### LC 84
```
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (i - index)*height)
                start = index
            stack.append((start, h))
        for i, h in stack:
            max_area = max(max_area, (len(heights)-i)*h)
        return max_area
```