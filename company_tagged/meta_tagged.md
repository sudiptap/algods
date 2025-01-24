## Binary Search
### Pattern Missing element in sorted array

## Heap

## Prefix Sum

## Stack
### Calculator Questions LC 224, LC 227
### 426. Convert Binary Search Tree to Sorted Doubly Linked List

### 921. Minimum Add to Make Parentheses Valid - constant space solution
### 636. Exclusive Time of Functions
### LC 536 Construct BT from string
### 1541. Minimum Insertions to Balance a Parentheses String


## Queue

## Got from leetcode Discuss

Minimum Remove to Make Valid Parentheses (45 times)
Valid Palindrome II (38 times)
Buildings With an Ocean View (34 times)
Binary Tree Vertical Order Traversal (33 times)
Kth Largest Element in an Array (31 times)
Random Pick with Weight (28 times)
Lowest Common Ancestor of a Binary Tree (26 times)
Simplify Path (25 times)
Dot Product of Two Sparse Vectors (24 times)
Merge Intervals (24 times)
Lowest Common Ancestor of a Binary Tree III (21 times)
Two Sum (19 times)
Valid Word Abbreviation (19 times)
Nested List Weight Sum (18 times)
Basic Calculator II (18 times)
Valid Palindrome (18 times)
Find Peak Element (17 times)
Binary Tree Right Side View (17 times)
Pow(x, n) (17 times)
Shortest Path in Binary Matrix (16 times)
K Closest Points to Origin (15 times)
Subarray Sum Equals K (15 times)
Minimum Add to Make Parentheses Valid (14 times)
Range Sum of BST (14 times)
Top K Frequent Elements (13 times)
Diameter of Binary Tree (12 times)
Find First and Last Position of Element in Sorted Array (12 times)
Merge Sorted Array (12 times)
Valid Parentheses (11 times)
Group Shifted Strings (11 times)
Vertical Order Traversal of a Binary Tree (11 times)
Roman to Integer (11 times)
Move Zeroes (10 times)
Continuous Subarray Sum (10 times)
Partition Equal Subset Sum (10 times)
Valid Number (10 times)
Number of Islands (9 times)
Copy List with Random Pointer (9 times)
3Sum (9 times)
Next Permutation (9 times)
Moving Average from Data Stream (9 times)
Best Time to Buy and Sell Stock (8 times)
Longest Substring Without Repeating Characters (8 times)
Custom Sort String (8 times)
LRU Cache (8 times)
Subsets (8 times)
Remove Nth Node From End of List (8 times)
Remove Invalid Parentheses (8 times)
Sum Root to Leaf Numbers (7 times)
Insert into a Sorted Circular Linked List (7 times)
Word Break (7 times)
Maximum Subarray (7 times)
Merge k Sorted Lists (7 times)
Binary Search Tree Iterator (7 times)
Add Two Numbers (7 times)
Max Consecutive Ones III (7 times)
Find Pivot Index (6 times)
Clone Graph (6 times)
Diagonal Traverse (6 times)
Word Search (6 times)
Group Anagrams (6 times)
Merge Two Sorted Lists (6 times)

## Top 100
56. Merge Intervals
48.0%
Medium
314. Binary Tree Vertical Order Traversal
55.4%
Medium
215. Kth Largest Element in an Array
67.2%
Medium
227. Basic Calculator II
44.3%
Medium
528. Random Pick with Weight
47.3%
Medium
1650. Lowest Common Ancestor of a Binary Tree III
80.6%
Medium
408. Valid Word Abbreviation
36.2%
Easy
680. Valid Palindrome II
41.5%
Easy
1249. Minimum Remove to Make Valid Parentheses
69.4%
Medium
560. Subarray Sum Equals K
44.2%
Medium
339. Nested List Weight Sum
84.4%
Medium
162. Find Peak Element
46.0%
Medium
1570. Dot Product of Two Sparse Vectors
89.9%
Medium
125. Valid Palindrome
48.9%
Easy
523. Continuous Subarray Sum
30.4%
Medium
71. Simplify Path
44.5%
Medium
347. Top K Frequent Elements
63.4%
Medium
236. Lowest Common Ancestor of a Binary Tree
64.1%
Medium
50. Pow(x, n)
35.7%
Medium
1762. Buildings With an Ocean View
80.0%
Medium
138. Copy List with Random Pointer
57.9%
Medium
791. Custom Sort String
71.1%
Medium
973. K Closest Points to Origin
67.0%
Medium
938. Range Sum of BST
87.1%
Easy
489. Robot Room Cleaner
76.9%
Hard
346. Moving Average from Data Stream
78.9%
Easy
1091. Shortest Path in Binary Matrix
48.2%
Medium
317. Shortest Distance from All Buildings
43.5%
Hard
987. Vertical Order Traversal of a Binary Tree
49.0%
Hard
498. Diagonal Traverse
61.2%
Medium
199. Binary Tree Right Side View
64.0%
Medium
282. Expression Add Operators
40.3%
Hard
636. Exclusive Time of Functions
62.7%
Medium
415. Add Strings
51.6%
Easy
670. Maximum Swap
49.1%
Medium
708. Insert into a Sorted Circular Linked List
36.7%
Medium
249. Group Shifted Strings
66.2%
Medium
426. Convert Binary Search Tree to Sorted Doubly Linked List
65.0%
Medium
65. Valid Number
20.4%
Hard
301. Remove Invalid Parentheses
48.6%
Hard
1216. Valid Palindrome III
49.3%
Hard
398. Random Pick Index
63.8%
Medium
1428. Leftmost Column with at Least a One
54.7%
Medium
163. Missing Ranges
34.2%
Easy
766. Toeplitz Matrix
69.1%
Easy
173. Binary Search Tree Iterator
73.2%
Medium
270. Closest Binary Search Tree Value
50.9%
Easy
2060. Check if an Original String Exists Given Two Encoded Strings
43.8%
Hard
921. Minimum Add to Make Parentheses Valid
74.6%
Medium
1891. Cutting Ribbons
49.8%
Medium

## LC filter by 30 days, 60 days and so on

https://leetcode.com/company/facebook/?favoriteSlug=facebook-thirty-days

Other problems from LC Discuss

https://leetcode.com/discuss/interview-question/354854/Facebook-or-Phone-Screen-or-Cut-Wood


## Last 6 Months
1249. Minimum Remove to Make Valid Parentheses
Med.

408. Valid Word Abbreviation
Easy *

314. Binary Tree Vertical Order Traversal
Med.

680. Valid Palindrome II
Easy *

215. Kth Largest Element in an Array
Med.

1650. Lowest Common Ancestor of a Binary Tree III
Med. *

528. Random Pick with Weight
Med. *

227. Basic Calculator II
Med. ** do a dry run

88. Merge Sorted Array
Easy

339. Nested List Weight Sum
Med.*

71. Simplify Path
Med.*

236. Lowest Common Ancestor of a Binary Tree
Med.

1570. Dot Product of Two Sparse Vectors
Med.*

560. Subarray Sum Equals K
Med. **
```
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        presum = 0
        ans = 0
        for idx, num in enumerate(nums):
            presum += num
            if (presum - k) in d:
                ans += d[(presum - k)]
            d[presum] = d.get(presum, 0) + 1
        return ans
```

50. Pow(x, n)
Med.

162. Find Peak Element
Med.

283. Move Zeroes
Easy

1762. Buildings With an Ocean View
Med. **
Trick : we don't need stack for this, O(1) solution is possible

56. Merge Intervals
Med. *

543. Diameter of Binary Tree
Easy *

## Oct 10

125. Valid Palindrome
Easy

1. Two Sum
Easy

938. Range Sum of BST
Easy

15. 3Sum
Med.**
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums or len(nums) == 0:
            return res
        
        nums.sort()
        
        for firstIdx in range(len(nums)):
            if firstIdx == 0 or (firstIdx > 0 and nums[firstIdx] != nums[firstIdx-1]):
                target = 0 - nums[firstIdx]
                low, high = firstIdx + 1, len(nums) - 1
                while low < high:
                    if nums[low] + nums[high] == target:
                        res.append([nums[firstIdx], nums[low], nums[high]])
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        high -= 1
                    elif target > nums[low] + nums[high]:
                        low += 1
                    else:
                        high -= 1
        return res
        
```

973. K Closest Points to Origin
Med.

1091. Shortest Path in Binary Matrix
Med. *

138. Copy List with Random Pointer
Med. **
```
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        m = {}
        curr = head
        newDummyHead = Node(-1)
        newCurr = newDummyHead
        while curr:
            #print(curr.val)
            newCurr.next = Node(curr.val)
            
            m[curr] = newCurr.next
            
            newCurr = newCurr.next
            curr = curr.next
        
        newCurr = newDummyHead.next
        curr = head
        
        while curr:
            #print(newCurr.val)
            newCurr.random = m[curr.random] if curr.random else None
            newCurr = newCurr.next
            curr = curr.next
        
        return newDummyHead.next
```

31. Next Permutation
Med. ** do a dry run
```
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
```

146. LRU Cache
Med. *

347. Top K Frequent Elements
Med.

199. Binary Tree Right Side View
Med.*

791. Custom Sort String
Med.

921. Minimum Add to Make Parentheses Valid
Med. ***
```
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openp, closep = 0, 0
        for ch in s:
            if ch == "(":
                openp += 1
            elif ch == ")":
                if openp > 0:
                    openp -= 1
                else:
                    closep += 1
        return openp + closep
```

200. Number of Islands
Med.

346. Moving Average from Data Stream
Easy ***
```
class MovingAverage:

    def __init__(self, size: int):
        self.dq = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.dq) < self.size:
            # add more element
            self.sum += val
            self.dq.append(val)
            return float(self.sum)/float(len(self.dq))
        else: # if len(self.dq) == self.size
            # popleft and then add 
            popped_left = self.dq.popleft()
            self.sum -= popped_left
            self.sum += val
            self.dq.append(val)
            return float(self.sum)/float(self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

23. Merge k Sorted Lists
Hard *

17. Letter Combinations of a Phone Number
Med.

827. Making A Large Island
Hard *

1004. Max Consecutive Ones III
Med. *

34. Find First and Last Position of Element in Sorted Array
Med.

## Oct 11

670. Maximum Swap
Med. **
```
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        #print(s)
        
        digits = [-1 for _ in range(0, 10)]
        #print(digits)
        
        for index, ch in enumerate(s):
            digit = int(ch)
            digits[digit] = max(digits[digit], index)
        
        #print(digits)
        
        for index, ch in enumerate(s):
            digit = int(ch)
            for biggerDigit in range(9, digit, -1):
                if digits[biggerDigit] > index:
                    # print(f"biggerDigit = {biggerDigit}, biggerDigit Loc = {digits[biggerDigit]}, digit = {digit}, s[digit] = {s[digit]}")
                    # swap
                    s[index], s[digits[biggerDigit]] = s[digits[biggerDigit]], s[index]
                    # return
                    res = ""
                    for i in s:
                        res += i
                    return int(res)
        
        return num
```

14. Longest Common Prefix
Easy

20. Valid Parentheses
Easy

133. Clone Graph
Med. **
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldtonew = {}
        
        def clone(node):
            if node in oldtonew:
                return oldtonew[node]
            
            copy = Node(node.val)
            oldtonew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None
        #return oldtonew[node]
```

129. Sum Root to Leaf Numbers
Med.

426. Convert Binary Search Tree to Sorted Doubly Linked List
Med. ***

986. Interval List Intersections
Med. *

65. Valid Number
Hard ***
```
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_dec = seen_expo = False
        for index, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in '+-':
                if (index > 0 and s[index-1] not in "Ee"):
                    return False
            elif ch in 'Ee':
                if seen_expo or not seen_digit:
                    return False
                seen_expo = True
                seen_digit = False
            elif ch == ".":
                if seen_dec or seen_expo:
                    return False
                seen_dec = True
            else:
                return False
        return seen_digit
```

498. Diagonal Traverse
Med. *

523. Continuous Subarray Sum
Med. **

Trick: Declare a map where remainder is key and value is the index where we see the remainder. 

```
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        psum = 0
        for idx in range(len(nums)):
            psum += nums[idx]
            rem = psum % k
            if rem in d:
                if idx - d[rem] >= 2:
                    return True
            else:
                d[rem] = idx
        
        return False
```

1539. Kth Missing Positive Number
Easy ***
```
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (right + left) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
```

2. Add Two Numbers
Med.

398. Random Pick Index
Med. *

987. Vertical Order Traversal of a Binary Tree
Hard *

5. Longest Palindromic Substring
Med. *

721. Accounts Merge
Med. *** (union find)
```
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res
```

708. Insert into a Sorted Circular Linked List
Med.

3. Longest Substring Without Repeating Characters
Med.

4. Median of Two Sorted Arrays
Hard ***
```
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        low, high = 0, len(A) - 1
        while True:
            i = (low + high) // 2
            j = half - i - 2
            
            a_left = A[i] if i>=0 else -sys.maxsize
            a_right = A[i+1] if (i+1) < len(A) else sys.maxsize
            
            b_left = B[j] if j>=0 else -sys.maxsize
            b_right = B[j+1] if (j+1) < len(B) else sys.maxsize
            
            # valid partition
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)
                # even
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                high = i - 1
            else:
                low = i + 1
```

415. Add Strings
Easy

636. Exclusive Time of Functions
Med. *** need practice
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

691. Stickers to Spell Word
Hard **
```
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_map = Counter(target)
        sticker_map = {}
        for sticker in stickers:
            sticker_map[sticker] = Counter(sticker)
        
        def stringify(map_):
            return "".join(f"{key}:{value}" for key, value in map_.items())

        q = deque()
        q.append([target_map, 0])
        visit = set()
        
        while q:
            cur_target_map, cur_count = q.popleft()
            #print(cur_target_map)
            if len(cur_target_map) == 0:
                return cur_count
            if stringify(cur_target_map) in visit:
                continue
            str_ = stringify(cur_target_map)
            #print(str_)
            visit.add(str_)
            # loop through each word and subtract
            for sticker in stickers:
                curr_sticker_map = sticker_map[sticker]
                # check if this sticker will contribute at all to the target
                leftover_map = (cur_target_map.copy() - curr_sticker_map)
                for key in leftover_map:
                    if leftover_map[key] <= 0:
                        leftover_map.remove(key)
                contrib = (leftover_map != cur_target_map.copy())
                if contrib:
                    #print(f"contrib is True")
                    
                    q.append([leftover_map.copy(), cur_count+1])
        
        return -1
```
2667. Create Hello World Function
Easy ***

78. Subsets
Med.

121. Best Time to Buy and Sell Stock
Easy

1047. Remove All Adjacent Duplicates In String
Easy

33. Search in Rotated Sorted Array
Med.

42. Trapping Rain Water
Hard **

76. Minimum Window Substring
Hard *

249. Group Shifted Strings
Med. 

766. Toeplitz Matrix
Easy

1868. Product of Two Run-Length Encoded Arrays
Med. *

70. Climbing Stairs
Easy

270. Closest Binary Search Tree Value
Easy

282. Expression Add Operators
Hard *** 

953. Verifying an Alien Dictionary
Easy *

7. Reverse Integer
Med.

525. Contiguous Array
Med. * 
Pattern: hasmap , store count of excess 1s as key and index where you observe it as value

647. Palindromic Substrings
Med. ***
Blueprint: https://www.youtube.com/watch?v=tGAMyZxlwuA

1768. Merge Strings Alternately
Easy

21. Merge Two Sorted Lists
Easy

38. Count and Say
Med. ***
source: https://www.youtube.com/watch?v=5uJitfSM3vk

53. Maximum Subarray
Med.

127. Word Ladder
Hard *

207. Course Schedule
Med. * Topological Sorting

658. Find K Closest Elements
Med.

9. Palindrome Number
Easy

13. Roman to Integer
Easy **

26. Remove Duplicates from Sorted Array
Easy *

48. Rotate Image
Med.

75. Sort Colors
Med. **
use counting sort TC O(n+k), k being the number of colors here

124. Binary Tree Maximum Path Sum
Hard

128. Longest Consecutive Sequence
Med.

140. Word Break II
Hard *

238. Product of Array Except Self
Med. *

273. Integer to English Words
Hard *** - I hate this question

1216. Valid Palindrome III
Hard, practice required

8. String to Integer (atoi)
Med. **

16. 3Sum Closest
Med.

19. Remove Nth Node From End of List
Med.

69. Sqrt(x)
Easy

118. Pascal's Triangle
Easy *

153. Find Minimum in Rotated Sorted Array
Med.

163. Missing Ranges
Easy *

173. Binary Search Tree Iterator
Med.

198. House Robber
Med.

253. Meeting Rooms II
Med. *

480. Sliding Window Median
Hard

489. Robot Room Cleaner
Hard ***

43. Multiply Strings
Med. *** - I hate this question

102. Binary Tree Level Order Traversal
Med. 

139. Word Break
Med. *

169. Majority Element
Easy *

219. Contains Duplicate II
Easy *

278. First Bad Version
Easy

301. Remove Invalid Parentheses
Hard *

394. Decode String
Med.

824. Goat Latin
Easy

1060. Missing Element in Sorted Array
Med. ***

1424. Diagonal Traverse II
Med. *


## Oct 13


10. Regular Expression Matching
Hard ***

11. Container With Most Water
Med. *

28. Find the Index of the First Occurrence in a String
Easy **

44. Wildcard Matching
Hard ***

49. Group Anagrams
Med.

62. Unique Paths
Med.

72. Edit Distance
Med. *

80. Remove Duplicates from Sorted Array II
Med. *

84. Largest Rectangle in Histogram
Hard ***

105. Construct Binary Tree from Preorder and Inorder Traversal
Med.

116. Populating Next Right Pointers in Each Node
Med. *

131. Palindrome Partitioning
Med. *

136. Single Number
Easy

210. Course Schedule II
Med. *

234. Palindrome Linked List
Easy *

235. Lowest Common Ancestor of a Binary Search Tree
Med. 

317. Shortest Distance from All Buildings
Hard *

333. Largest BST Subtree
Med. 

348. Design Tic-Tac-Toe
Med. *

392. Is Subsequence
Easy *

## Oct 14

443. String Compression
Med.

825. Friends Of Appropriate Ages
Med.

863. All Nodes Distance K in Binary Tree
Med.

1011. Capacity To Ship Packages Within D Days
Med.

1209. Remove All Adjacent Duplicates in String II
Med.

24. Swap Nodes in Pairs
Med. **

27. Remove Element
Easy

37. Sudoku Solver
Hard *

55. Jump Game
Med.

57. Insert Interval
Med. *

67. Add Binary
Easy *

79. Word Search
Med. *

113. Path Sum II
Med. *

179. Largest Number
Med.

268. Missing Number
Easy

269. Alien Dictionary
Hard **
```
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # first build the pmap
        # map holding characters -> following characters learnt from the words
        pmap = {c: set() for word in words for c in word}

        # populate the pmap
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            # app, apple ->valid
            # apple, app -> invalid
            minlen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word2 == word1[:minlen]:
                return ""
            # if not then, loop over lenght of minlen and check for characters mismatch
            for j in range(minlen):
                if word1[j] != word2[j]:
                    pmap[word1[j]].add(word2[j])
                    break
        
        # declare visit and cycle 
        visit = set()
        cycle = set()
        res = []
        # loop over pmap and see if you find a cycle
        def dfs(key):
            if key in cycle:
                return True
            if key in visit:
                return False
            cycle.add(key)
            for nei in pmap[key]:
                if dfs(nei):
                    return True
            cycle.remove(key)
            visit.add(key)
            res.append(key)
            return False
        
        for key, value in pmap.items():
            if dfs(key):
                return ""
        res.reverse()
        return "".join(res)

```

286. Walls and Gates
Med. *

341. Flatten Nested List Iterator
Med. *

350. Intersection of Two Arrays II
Easy *

380. Insert Delete GetRandom O(1)
Med. *

383. Ransom Note
Easy

494. Target Sum
Med. *

539. Minimum Time Difference
Med. **

605. Can Place Flowers
Easy

617. Merge Two Binary Trees
Easy *

739. Daily Temperatures
Med.

934. Shortest Bridge
Med. *

977. Squares of a Sorted Array
Easy

1443. Minimum Time to Collect All Apples in a Tree
Med. * https://www.youtube.com/watch?v=Xdt5Z583auM

1752. Check if Array Is Sorted and Rotated
Easy *

22. Generate Parentheses
Med. *

29. Divide Two Integers
Med. **

54. Spiral Matrix
Med. *

82. Remove Duplicates from Sorted List II
Med.

104. Maximum Depth of Binary Tree
Easy

206. Reverse Linked List
Easy **

231. Power of Two
Easy

266. Palindrome Permutation
Easy

332. Reconstruct Itinerary
Hard ***

378. Kth Smallest Element in a Sorted Matrix
Med. ***

410. Split Array Largest Sum
Hard **

419. Battleships in a Board
Med. *

493. Reverse Pairs
Hard **

496. Next Greater Element I
Easy

540. Single Element in a Sorted Array
Med. *

633. Sum of Square Numbers
Med. **

695. Max Area of Island
Med. *

725. Split Linked List in Parts
Med. *, practice LL

704. Binary Search
Easy

622. Design Circular Queue
Med. *

875. Koko Eating Bananas
Med. *

958. Check Completeness of a Binary Tree
Med. **

995. Minimum Number of K Consecutive Bit Flips
Hard ** I hate bitwise

1122. Relative Sort Array
Easy

1778. Shortest Path in a Hidden Grid
Med. ***
Use DFS to identify the target and the grid, then bfs to identify the shortest path

18. 4Sum
Med. *

25. Reverse Nodes in k-Group
Hard ** practice LL

40. Combination Sum II
Med. *

58. Length of Last Word
Easy

66. Plus One
Easy

73. Set Matrix Zeroes
Med. *
```
```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
        row0 = False
        
        # traverse the matrix ans set the first row and col cells zero if
        # matrix[row][col] is zero
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row > 0:
                        matrix[0][col] = 0
                        matrix[row][0] = 0
                    else:
                        row0 = True
        
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    # means the entire column should be 0
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0
            
        if row0:
            for col in range(COLS):
                matrix[0][col] = 0

74. Search a 2D Matrix
Med.

90. Subsets II
Med. *

91. Decode Ways
Med. *

103. Binary Tree Zigzag Level Order Traversal
Med. 

114. Flatten Binary Tree to Linked List
Med. ***
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

142. Linked List Cycle II
Med. *

145. Binary Tree Postorder Traversal
Easy

151. Reverse Words in a String
Med. *

152. Maximum Product Subarray
Med. **

155. Min Stack
Med.

161. One Edit Distance
Med. *

168. Excel Sheet Column Title
Easy ***

189. Rotate Array
Med. *

191. Number of 1 Bits
Easy *

208. Implement Trie (Prefix Tree)
Med. *

221. Maximal Square
Med. *

242. Valid Anagram
Easy

246. Strobogrammatic Number
Easy *

257. Binary Tree Paths
Easy

304. Range Sum Query 2D - Immutable
Med. **

322. Coin Change
Med. *

328. Odd Even Linked List
Med. **

330. Patching Array
Hard *** 


Stopping at half way here
--------------------------

387. First Unique Character in a String
Easy

404. Sum of Left Leaves
Easy

424. Longest Repeating Character Replacement
Med. *

463. Island Perimeter
Easy *

485. Max Consecutive Ones
Easy

490. The Maze
Med. *

536. Construct Binary Tree from String
Med. *

547. Number of Provinces
Med. *

735. Asteroid Collision
Med.

778. Swim in Rising Water
Hard *

796. Rotate String
Easy *
 
857. Minimum Cost to Hire K Workers
Hard ***

885. Spiral Matrix III
Med. ***

896. Monotonic Array
Easy

912. Sort an Array
Med.

918. Maximum Sum Circular Subarray
Med. *

930. Binary Subarrays With Sum
Med. ***

509. Fibonacci Number
Easy

983. Minimum Cost For Tickets
Med. *

1013. Partition Array Into Three Parts With Equal Sum
Easy *

1213. Intersection of Three Sorted Arrays
Easy ***

## Oct 17

## practice as many questions possible below, will only mark **


1428. Leftmost Column with at Least a One
Med. *

1344. Angle Between Hands of a Clock
Med. ***

1371. Find the Longest Substring Containing Vowels in Even Counts
Med. ***
```
Pattern: 
```

2265. Count Nodes Equal to Average of Subtree
Med.

2235. Add Two Integers
Easy

2824. Count Pairs Whose Sum is Less than Target
Easy

3043. Find the Length of the Longest Common Prefix
Med. **
```
Trie Pattern

```

36. Valid Sudoku
Med.

45. Jump Game II
Med. **
```
Pattern : if I am at index i, I wat to track the range of indices I can reach from here, e.g.
[2,3,1,1,4] when i = 0 we can reach [1,2] indices with step 1, then 1+1, 1+2, 1+3 ={2,3,4} as 1,2,3 are in the range of 
nums[1] == 3, for i=2, 2+nums[2] = 3, hence [2,4] in step 2, at this point we identify we reached index 4 hence answer is 2 steps.
so, keep track of the range of indices we can reach after everystep.
```

46. Permutations
Med. ***

61. Rotate List
Med. **

63. Unique Paths II
Med.

98. Validate Binary Search Tree
Med.

117. Populating Next Right Pointers in Each Node II
Med. *** Try the O(1) space solution 

135. Candy
Hard ***

143. Reorder List
Med. **

148. Sort List
Med. **

149. Max Points on a Line
Hard **
```
use a hasmap to store slope x2-x1/y2-y1 as key or points p1 = (x1,y1) and p2 = (x2,y2) and number of points
on the slope as value.
```

209. Minimum Size Subarray Sum
Med. ***

212. Word Search II
Hard *** 
```
super imporatnat to learn Prefix Tree, DFS

class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def insert(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.insert(word)
        res = set()
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, word, node):
            # check if row, col should be visited
            if row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visit or (board[row][col] not in node.children):
                return
            
            visit.add((row, col))
            ch = board[row][col]
            node = node.children[ch]
            word += ch
            if node.isWord:
                res.add(word)
            
            dfs(row-1, col, node, word)
            dfs(row+1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row, col-1, node, word)

            visit.remove((row, col))
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, "", root)
        return list(res)
```

217. Contains Duplicate
Easy 

224. Basic Calculator
Hard ***

226. Invert Binary Tree
Easy *

237. Delete Node in a Linked List
Med.

277. Find the Celebrity
Med.

295. Find Median from Data Stream
Hard ***

297. Serialize and Deserialize Binary Tree
Hard ***

299. Bulls and Cows
Med. ** hate this question

329. Longest Increasing Path in a Matrix
Hard ***

334. Increasing Triplet Subsequence
Med. ***


--- Nov 17
337. House Robber III
Med.

344. Reverse String
Easy

377. Combination Sum IV
Med.

386. Lexicographical Numbers
Med. ***

399. Evaluate Division
Med. *

409. Longest Palindrome
Easy

416. Partition Equal Subset Sum
Med.

437. Path Sum III
Med. ***
```
pattern
map[cur_sum] -> count
res += map[curr_sum - target_sum]
return res
```

438. Find All Anagrams in a String
Med.

450. Delete Node in a BST
Med. **

461. Hamming Distance
Easy **

477. Total Hamming Distance
Med. **

535. Encode and Decode TinyURL
Med.

554. Brick Wall
Med. **

556. Next Greater Element III
Med.

621. Task Scheduler
Med. *

643. Maximum Average Subarray I
Easy

673. Number of Longest Increasing Subsequence
Med. **
```
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        m, dp, cnt = 0, [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1: dp[i], cnt[i] = dp[j]+1, cnt[j]
                    elif dp[i] == dp[j]+1: cnt[i] += cnt[j]
            m = max(m, dp[i])                        
        return sum(c for l, c in zip(dp, cnt) if l == m)
```

689. Maximum Sum of 3 Non-Overlapping Subarrays
Hard ***

785. Is Graph Bipartite?
Med.

852. Peak Index in a Mountain Array
Med.

865. Smallest Subtree with all the Deepest Nodes
Med. **

876. Middle of the Linked List
Easy

959. Regions Cut By Slashes
Med. ***

998. Maximum Binary Tree II
Med. *

1108. Defanging an IP Address
Easy

1146. Snapshot Array
Med.

1331. Rank Transform of an Array
Easy

1353. Maximum Number of Events That Can Be Attended
Med. **
```
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # sort by start time
        events.sort()

        days = max(end for start,end in events)
        ans = 0

        heap = []
        eventId = 0
        for day in range(1, days+1):
            while events[eventId][0] == day:
                # all events thats starts that day goes in the heap
                heapq.heappush(heap, events[eventId][1])
                eventId += 1
            # remove all events from the heap that ended already
            while heap:
                if heap[0] < day:
                    heapq.heappop(heap)
            
            # all the events in heap can be taken this day
            # we will take the one on the top since this ends first
            if heap:
                ans += 1
        return ans
```

1367. Linked List in Binary Tree
Med. **

1460. Make Two Arrays Equal by Reversing Subarrays
Easy

1590. Make Sum Divisible by P
Med. ** LC 560 , LC 974, LC 1074 same pattern

1586. Binary Search Tree Iterator II
Med. **

1608. Special Array With X Elements Greater Than or Equal X
Easy **

1609. Even Odd Tree
Med.

1662. Check If Two String Arrays are Equivalent
Easy

1688. Count of Matches in Tournament
Easy

1790. Check if One String Swap Can Make Strings Equal
Easy

1810. Minimum Path Cost in a Hidden Grid
Med. **

1838. Frequency of the Most Frequent Element
Med. ***

1826. Faulty Sensor
Easy

1920. Build Array from Permutation
Easy

2104. Sum of Subarray Ranges
Med. ***
Prequisite pattern : sum of subarray minimum
Prereq pattern: Previous smaller element, previous larger element, Next smaller/ larger element

2210. Count Hills and Valleys in an Array
Easy

2487. Remove Nodes From Linked List
Med.

2553. Separate the Digits in an Array
Easy

3110. Score of a String
Easy

3206. Alternating Groups I
Easy

3202. Find the Maximum Length of Valid Subsequence II
Med.

6. Zigzag Conversion
Med.

12. Integer to Roman
Med.

32. Longest Valid Parentheses
Hard

41. First Missing Positive
Hard

47. Permutations II
Med.

51. N-Queens
Hard

52. N-Queens II
Hard

68. Text Justification
Hard

81. Search in Rotated Sorted Array II
Med.

85. Maximal Rectangle
Hard

86. Partition List
Med.

92. Reverse Linked List II
Med.

93. Restore IP Addresses
Med.

96. Unique Binary Search Trees
Med.

111. Minimum Depth of Binary Tree
Easy

122. Best Time to Buy and Sell Stock II
Med.

123. Best Time to Buy and Sell Stock III
Hard

126. Word Ladder II
Hard ***

130. Surrounded Regions
Med.

134. Gas Station
Med. **

137. Single Number II
Med. bit manipulation

144. Binary Tree Preorder Traversal
Easy

150. Evaluate Reverse Polish Notation
Med.

157. Read N Characters Given Read4
Easy ***

158. Read N Characters Given read4 II - Call Multiple Times
Hard ***

160. Intersection of Two Linked Lists
Easy

167. Two Sum II - Input Array Is Sorted
Med.

190. Reverse Bits
Easy

204. Count Primes
Med. Math problem **

205. Isomorphic Strings
Easy

211. Design Add and Search Words Data Structure
Med.

214. Shortest Palindrome
Hard not Meta question

218. The Skyline Problem
Hard ***, do a dry run

222. Count Complete Tree Nodes
Easy ***

228. Summary Ranges
Easy *

230. Kth Smallest Element in a BST
Med.

252. Meeting Rooms
Easy

261. Graph Valid Tree
Med.
patern: ***

263. Ugly Number
Easy **

264. Ugly Number II
Med. **

265. Paint House II
Hard  https://www.youtube.com/watch?v=jGywRalvoRw

271. Encode and Decode Strings
Med.

274. H-Index
Med.

275. H-Index II
Med.

285. Inorder Successor in BST
Med.

290. Word Pattern
Easy

311. Sparse Matrix Multiplication
Med.

325. Maximum Size Subarray Sum Equals k
Med. **

340. Longest Substring with At Most K Distinct Characters
Med. practice this once

345. Reverse Vowels of a String
Easy

349. Intersection of Two Arrays
Easy

371. Sum of Two Integers
Med.

373. Find K Pairs with Smallest Sums
Med.

381. Insert Delete GetRandom O(1) - Duplicates allowed
Hard **

417. Pacific Atlantic Water Flow
Med.

432. All O`one Data Structure
Hard ***

435. Non-overlapping Intervals
Med. **



Dec 21
--------

455. Assign Cookies
Easy

468. Validate IP Address
Med.

502. IPO
Hard

504. Base 7
Easy

1721. Swapping Nodes in a Linked List
Med.

529. Minesweeper
Med.

530. Minimum Absolute Difference in BST
Easy

542. 01 Matrix
Med.

545. Boundary of Binary Tree
Med.

567. Permutation in String
Med.

570. Managers with at Least 5 Direct Reports
Med.

572. Subtree of Another Tree
Easy

578. Get Highest Answer Rate Question
Med.

588. Design In-Memory File System
Hard

595. Big Countries
Easy

602. Friend Requests II: Who Has the Most Friends
Med.

610. Triangle Judgement
Easy

628. Maximum Product of Three Numbers
Easy

629. K Inverse Pairs Array
Hard

637. Average of Levels in Binary Tree
Easy

639. Decode Ways II
Hard

642. Design Search Autocomplete System
Hard

645. Set Mismatch
Easy

653. Two Sum IV - Input is a BST
Easy

674. Longest Continuous Increasing Subsequence
Easy

678. Valid Parenthesis String
Med.

711. Number of Distinct Islands II
Hard ****

714. Best Time to Buy and Sell Stock with Transaction Fee
Med.

724. Find Pivot Index
Easy

727. Minimum Window Subsequence
Hard

733. Flood Fill
Easy

745. Prefix and Suffix Search
Hard

750. Number Of Corner Rectangles
Med.

764. Largest Plus Sign
Med.

767. Reorganize String
Med.

700. Search in a Binary Search Tree
Easy

703. Kth Largest Element in a Stream
Easy

784. Letter Case Permutation
Med.

787. Cheapest Flights Within K Stops
Med.

705. Design HashSet
Easy

706. Design HashMap
Easy

801. Minimum Swaps To Make Sequences Increasing
Hard

843. Guess the Word
Hard

860. Lemonade Change
Easy

893. Groups of Special-Equivalent Strings
Med.

905. Sort Array By Parity
Easy

907. Sum of Subarray Minimums
Med.

968. Binary Tree Cameras
Hard

981. Time Based Key-Value Store
Med.

989. Add to Array-Form of Integer
Easy

994. Rotting Oranges
Med.

1002. Find Common Characters
Easy

1021. Remove Outermost Parentheses
Easy

1033. Moving Stones Until Consecutive
Med.

1040. Moving Stones Until Consecutive II
Med.

1043. Partition Array for Maximum Sum
Med.

1045. Customers Who Bought All Products
Med.

1052. Grumpy Bookstore Owner
Med.

1076. Project Employees II
Easy

1077. Project Employees III
Med.

1092. Shortest Common Supersequence
Hard

550. Game Play Analysis IV
Med.

1113. Reported Posts
Easy

1123. Lowest Common Ancestor of Deepest Leaves
Med.

1287. Element Appearing More Than 25% In Sorted Array
Easy

1137. N-th Tribonacci Number
Easy

1132. Reported Posts II
Med.

1140. Stone Game II
Med.

1142. User Activity for the Past 30 Days II
Easy

1143. Longest Common Subsequence
Med.

1236. Web Crawler
Med.

1361. Validate Binary Tree Nodes
Med.

1514. Path with Maximum Probability
Med.

1225. Report Contiguous Dates
Hard

1242. Web Crawler Multithreaded
Med.

1241. Number of Comments per Post
Easy

1255. Maximum Score Words Formed by Letters
Hard

2303. Calculate Amount Paid in Taxes
Easy

1264. Page Recommendations
Med.

1281. Subtract the Product and Sum of Digits of an Integer
Easy

1309. Decrypt String from Alphabet to Integer Mapping
Easy

1312. Minimum Insertion Steps to Make a String Palindrome
Hard

1322. Ads Performance
Easy

1357. Apply Discount Every n Orders
Med.

1358. Number of Substrings Containing All Three Characters
Med.

1338. Reduce Array Size to The Half
Med.

1352. Product of the Last K Numbers
Med.

1341. Movie Rating
Med.

1386. Cinema Seat Allocation
Med.

1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
Easy

1431. Kids With the Greatest Number of Candies
Easy

1398. Customers Who Bought Products A and B but Not C
Med.

1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
Hard

1453. Maximum Number of Darts Inside of a Circular Dartboard
Hard

1445. Apples & Oranges
Med.

1482. Minimum Number of Days to Make m Bouquets
Med.

1512. Number of Good Pairs
Easy

1541. Minimum Insertions to Balance a Parentheses String
Med.

1522. Diameter of N-Ary Tree
Med.

1581. Customer Who Visited but Did Not Make Any Transactions
Easy

1631. Path With Minimum Effort
Med.

1718. Construct the Lexicographically Largest Valid Sequence
Med.

1748. Sum of Unique Elements
Easy

1773. Count Items Matching a Rule
Easy

1854. Maximum Population Year
Easy

1877. Minimize Maximum Pair Sum in Array
Med.

1863. Sum of All Subset XOR Totals
Easy

1926. Nearest Exit from Entrance in Maze
Med.

1928. Minimum Cost to Reach Destination in Time
Hard

1892. Page Recommendations II
Hard

1922. Count Good Numbers
Med.

1947. Maximum Compatibility Score Sum
Med.

1934. Confirmation Rate
Med.

1976. Number of Ways to Arrive at Destination
Med.

1949. Strong Friendship
Med.

1973. Count Nodes Equal to Sum of Descendants
Med.

2022. Convert 1D Array Into 2D Array
Easy

2014. Longest Subsequence Repeated k Times
Hard

2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
Med.

2097. Valid Arrangement of Pairs
Hard

2096. Step-By-Step Directions From a Binary Tree Node to Another
Med.

2199. Finding the Topic of Each Post
Hard

2281. Sum of Total Strength of Wizards
Hard

2289. Steps to Make Array Non-decreasing
Med.

2365. Task Scheduler II
Med.

2419. Longest Subarray With Maximum Bitwise AND
Med.

2452. Words Within Two Edits of Dictionary
Med.

2469. Convert the Temperature
Easy

2596. Check Knight Tour Configuration
Med.

2678. Number of Senior Citizens
Easy

2707. Extra Characters in a String
Med.

2704. To Be Or Not To Be
Easy

2807. Insert Greatest Common Divisors in Linked List
Med.

2915. Length of the Longest Subsequence That Sums to Target
Med.

3016. Minimum Number of Pushes to Type Word II
Med.

3165. Maximum Sum of Subsequence With Non-adjacent Elements
Hard

3186. Maximum Total Damage With Spell Casting
Med.

3164. Find the Number of Good Pairs II
Med.

## Greedy/ Divide and Conquer
1382. Balance an Binary Search Tree
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        
        def in_order_traverse(root):
            if root is None:return
            in_order_traverse(root.left)
            nodes.append(root)
            in_order_traverse(root.right)
        
        def build_balanced_tree(left, right):
            if left>right:return None
            mid = (left+right)//2
            root = nodes[mid]
            root.left = build_balanced_tree(left, mid-1)
            root.right = build_balanced_tree(mid+1, right)
            return root
        in_order_traverse(root)
        return build_balanced_tree(0, len(nodes)-1)
        
```

All Heaps
----------
Status
Title
Solution
Acceptance
Difficulty
Frequency

215. Kth Largest Element in an Array
67.4%
Medium
973. K Closest Points to Origin
67.4%
Medium
347. Top K Frequent Elements
63.8%
Medium
23. Merge k Sorted Lists
55.2%
Hard
1424. Diagonal Traverse II
57.5%
Medium
480. Sliding Window Median
38.7%
Hard
253. Meeting Rooms II
51.8%
Medium
378. Kth Smallest Element in a Sorted Matrix
63.1%
Medium
658. Find K Closest Elements
48.2%
Medium
295. Find Median from Data Stream
52.7%
Hard
857. Minimum Cost to Hire K Workers
63.5%
Hard
1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
62.0%
Hard
1810. Minimum Path Cost in a Hidden Grid
58.3%
Medium
767. Reorganize String
55.5%
Medium
2034. Stock Price Fluctuation
48.6%
Medium
1094. Car Pooling
56.0%
Medium
2611. Mice and Cheese
46.7%
Medium
1845. Seat Reservation Manager
69.9%
Medium
272. Closest Binary Search Tree Value II
59.8%
Hard
239. Sliding Window Maximum
47.1%
Hard
505. The Maze II
53.9%
Medium
1985. Find the Kth Largest Integer in the Array
46.2%
Medium
1353. Maximum Number of Events That Can Be Attended
32.7%
Medium
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
56.7%
Medium
2231. Largest Number After Digit Swaps by Parity
62.8%
Easy
778. Swim in Rising Water
62.0%
Hard
407. Trapping Rain Water II
48.7%
Hard
632. Smallest Range Covering Elements from K Lists
69.8%
Hard
1631. Path With Minimum Effort
60.7%
Medium
703. Kth Largest Element in a Stream
59.5%
Easy
451. Sort Characters By Frequency
73.4%
Medium
502. IPO
53.0%
Hard
218. The Skyline Problem
43.4%
Hard
862. Shortest Subarray with Sum at Least K
32.2%
Hard
787. Cheapest Flights Within K Stops
39.9%
Medium
912. Sort an Array
57.3%
Medium
373. Find K Pairs with Smallest Sums
40.3%
Medium
621. Task Scheduler
60.8%
Medium
1268. Search Suggestions System
65.1%
Medium
1046. Last Stone Weight
65.7%
Easy
642. Design Search Autocomplete System
49.2%
Hard


Binary Search
-------------
528. Random Pick with Weight
47.9%
Medium
162. Find Peak Element
46.3%
Medium
270. Closest Binary Search Tree Value - *
50.4%
Easy
1004. Max Consecutive Ones III
64.9%
Medium
1539. Kth Missing Positive Number
61.5%
Easy
825. Friends Of Appropriate Ages
48.6%
Medium
1060. Missing Element in Sorted Array - *
58.0%
Medium
378. Kth Smallest Element in a Sorted Matrix - *
63.1%
Medium
34. Find First and Last Position of Element in Sorted Array
45.8%
Medium
658. Find K Closest Elements - *
48.2%
Medium
1891. Cutting Ribbons - *
51.3%
Medium
1011. Capacity To Ship Packages Within D Days- *
71.1%
Medium
1498. Number of Subsequences That Satisfy the Given Sum Condition - *
43.8%
Medium
1213. Intersection of Three Sorted Arrays - *
80.2%
Easy
4. Median of Two Sorted Arrays - **
42.4%
Hard
1055. Shortest Way to Form String
60.7%
Medium
713. Subarray Product Less Than K - *
52.2%
Medium
33. Search in Rotated Sorted Array
42.1%
Medium
1062. Longest Repeating Substring
62.6%
Medium
875. Koko Eating Bananas
48.7%
Medium
633. Sum of Square Numbers
36.5%
Medium
1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows - ** hard question
62.0%
Hard
3186. Maximum Total Damage With Spell Casting
27.0%
Medium
278. First Bad Version
45.3%
Easy
1428. Leftmost Column with at Least a One - code    
54.8%
Medium
540. Single Element in a Sorted Array
59.2%
Medium
74. Search a 2D Matrix - 
pattern: 2d to 1d array id_index//num_cols = row_index, id_index%num_cols = col_index
51.5%
Medium
1671. Minimum Number of Removals to Make Mountain Array - ** not a BinSearch question, LIS variant
55.0%
Hard
2468. Split Message Based on Limit - no solutions
43.2%
Hard
3161. Block Placement Queries - **
15.3%
Hard
2501. Longest Square Streak in an Array
53.1%
Medium
367. Valid Perfect Square
44.0%
Easy
778. Swim in Rising Water
62.0%
Hard
1574. Shortest Subarray to be Removed to Make Array Sorted ** not BinSrch
51.8%
Medium
2981. Find Longest Special Substring That Occurs Thrice I ** 
62.3%
Medium
1095. Find in Mountain Array - code
40.2%
Hard
240. Search a 2D Matrix II
54.1%
Medium
153. Find Minimum in Rotated Sorted Array - *
51.9%
Medium
81. Search in Rotated Sorted Array II
38.4%
Medium
852. Peak Index in a Mountain Array
67.9%
Medium
350. Intersection of Two Arrays II
58.8%
Easy
1631. Path With Minimum Effort - djikstra variant
60.7%
Medium
287. Find the Duplicate Number 
62.1%
Medium
1901. Find a Peak Element II
52.6%
Medium
362. Design Hit Counter
68.9%
Medium
167. Two Sum II - Input Array Is Sorted
62.6%
Medium
862. Shortest Subarray with Sum at Least K - monotonic queue, sliding window
32.2%
Hard
1608. Special Array With X Elements Greater Than or Equal X - *
66.8%
Easy
410. Split Array Largest Sum - code
57.1%
Hard
1838. Frequency of the Most Frequent Element - sliding window
44.0%
Medium
493. Reverse Pairs
31.5%
Hard
69. Sqrt(x)
39.8%
Easy
222. Count Complete Tree Nodes
68.4%
Easy
349. Intersection of Two Arrays
75.8%
Easy
1268. Search Suggestions System
65.1%
Medium
209. Minimum Size Subarray Sum
48.4%
Medium
300. Longest Increasing Subsequence
56.9%
Medium
1283. Find the Smallest Divisor Given a Threshold
62.2%
Medium
704. Binary Search
58.9%
Easy
1482. Minimum Number of Days to Make m Bouquets
55.4%
Medium
981. Time Based Key-Value Store - code
49.3%
Medium
268. Missing Number
68.9%
Easy
35. Search Insert Position
48.0%
Easy
275. H-Index II
38.6%
Medium
2824. Count Pairs Whose Sum is Less than Target
87.4%
Easy

## Sliding Window

1004. Max Consecutive Ones III
64.9%
Medium
480. Sliding Window Median
38.7%
Hard
76. Minimum Window Substring
44.4%
Hard
727. Minimum Window Subsequence
43.5%
Hard
658. Find K Closest Elements
48.2%
Medium
219. Contains Duplicate II
47.6%
Easy
1358. Number of Substrings Containing All Three Characters
68.4%
Medium
643. Maximum Average Subarray I
44.4%
Easy
713. Subarray Product Less Than K
52.2%
Medium
2461. Maximum Sum of Distinct Subarrays With Length K **
42.8%
Medium

'''
class Solution:
    def maximumSubarraySum(self, nums, k):
        left, right = 0, 0
        chars = set()
        maxsum = 0
        cursum = 0
        while right < len(nums):
            while left < right and nums[right] in chars:
                cursum -= nums[left]
                chars.remove(nums[left])
                left += 1
            chars.add(nums[right])
            cursum += nums[right]
            if len(chars) == right - left + 1 == k:
                maxsum = max(maxsum, cursum)
                cursum -= nums[left]
                chars.remove(nums[left])
                left += 1
            right += 1

        
        return maxsum
        
'''

995. Minimum Number of K Consecutive Bit Flips
62.7%
Hard
424. Longest Repeating Character Replacement
56.1%
Medium
3097. Shortest Subarray With OR at Least K II
50.5%
Medium
3. Longest Substring Without Repeating Characters
36.0%
Medium
239. Sliding Window Maximum
47.1%
Hard
904. Fruit Into Baskets
45.4%
Medium
2090. K Radius Subarray Averages
46.1%
Medium
2516. Take K of Each Character From Left and Right *
51.9%
Medium
340. Longest Substring with At Most K Distinct Characters
49.2%
Medium
930. Binary Subarrays With Sum **
64.7%
Medium
2962. Count Subarrays Where Max Element Appears at Least K Times **
58.7%
Medium
1052. Grumpy Bookstore Owner
64.1%
Medium
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit *
56.7%
Medium
2981. Find Longest Special Substring That Occurs Thrice I *
62.3%
Medium
438. Find All Anagrams in a String
51.7%
Medium
632. Smallest Range Covering Elements from K Lists
69.8%
Hard
1493. Longest Subarray of 1's After Deleting One Element
68.5%
Medium
862. Shortest Subarray with Sum at Least K
32.2%
Hard
1838. Frequency of the Most Frequent Element
44.0%
Medium
209. Minimum Size Subarray Sum
48.5%
Medium
30. Substring with Concatenation of All Words
32.7%
Hard
992. Subarrays with K Different Integers
64.8%
Hard
567. Permutation in String
46.7%
Medium



Practice Frequently asked Questions
-----------------------------------
LC 296
LC 1091
LC 317
LC 1275
LC 339

Last 3 Months
----

3 months
1. Two Sum
54.7%
Easy

2. Add Two Numbers
45.1%
Med.

3. Longest Substring Without Repeating Characters
36.1%
Med.

4. Median of Two Sorted Arrays
42.5%
Hard

5. Longest Palindromic Substring
35.1%
Med.

7. Reverse Integer
29.7%
Med.

8. String to Integer (atoi)
18.5%
Med.

9. Palindrome Number
58.3%
Easy

10. Regular Expression Matching
28.8%
Hard

14. Longest Common Prefix
44.6%
Easy

15. 3Sum
36.1%
Med.

17. Letter Combinations of a Phone Number
62.7%
Med.

20. Valid Parentheses
41.6%
Easy

23. Merge k Sorted Lists
55.3%
Hard

26. Remove Duplicates from Sorted Array
59.0%
Easy

1004. Max Consecutive Ones III
64.9%
Med.

31. Next Permutation
42.0%
Med.

33. Search in Rotated Sorted Array
42.1%
Med.

34. Find First and Last Position of Element in Sorted Array
45.9%
Med.

38. Count and Say
57.5%
Med.

42. Trapping Rain Water
63.9%
Hard

43. Multiply Strings
41.6%
Med.

48. Rotate Image
76.8%
Med.

49. Group Anagrams
70.1%
Med.

50. Pow(x, n)
36.2%
Med.

53. Maximum Subarray
51.6%
Med.

55. Jump Game
39.0%
Med.

56. Merge Intervals
48.6%
Med.

57. Insert Interval
42.7%
Med.

986. Interval List Intersections
72.3%
Med.

987. Vertical Order Traversal of a Binary Tree
50.0%
Hard

65. Valid Number
20.9%
Hard

70. Climbing Stairs
53.3%
Easy

71. Simplify Path
45.9%
Med.

75. Sort Colors
66.0%
Med.

78. Subsets
80.0%
Med.

88. Merge Sorted Array
51.9%
Easy

102. Binary Tree Level Order Traversal
69.4%
Med.

118. Pascal's Triangle
76.2%
Easy

121. Best Time to Buy and Sell Stock
54.6%
Easy

124. Binary Tree Maximum Path Sum
40.8%
Hard

125. Valid Palindrome
49.8%
Easy

127. Word Ladder
41.4%
Hard

128. Longest Consecutive Sequence
47.5%
Med.

129. Sum Root to Leaf Numbers
67.6%
Med.

133. Clone Graph
60.6%
Med.

138. Copy List with Random Pointer
59.0%
Med.

139. Word Break
47.7%
Med.

146. LRU Cache
44.1%
Med.

1091. Shortest Path in Binary Matrix
48.9%
Med.

153. Find Minimum in Rotated Sorted Array
51.9%
Med.

1216. Valid Palindrome III
49.2%
Hard

162. Find Peak Element
46.3%
Med.

173. Binary Search Tree Iterator
74.0%
Med.

199. Binary Tree Right Side View
65.0%
Med.

200. Number of Islands
61.2%
Med.

207. Course Schedule
48.2%
Med.

215. Kth Largest Element in an Array
67.4%
Med.

219. Contains Duplicate II
47.7%
Easy

227. Basic Calculator II
45.0%
Med.

235. Lowest Common Ancestor of a Binary Search Tree
67.1%
Med.

236. Lowest Common Ancestor of a Binary Tree
65.2%
Med.

238. Product of Array Except Self
67.2%
Med.

253. Meeting Rooms II
51.8%
Med.

269. Alien Dictionary
36.3%
Hard

270. Closest Binary Search Tree Value
50.4%
Easy

282. Expression Add Operators
40.8%
Hard

283. Move Zeroes
62.4%
Easy

314. Binary Tree Vertical Order Traversal
56.3%
Med.

317. Shortest Distance from All Buildings
43.7%
Hard

339. Nested List Weight Sum
85.0%
Med.

346. Moving Average from Data Stream
79.4%
Easy

347. Top K Frequent Elements
63.9%
Med.

348. Design Tic-Tac-Toe
58.4%
Med.

1249. Minimum Remove to Make Valid Parentheses
70.0%
Med.

380. Insert Delete GetRandom O(1)
54.8%
Med.

398. Random Pick Index
64.2%
Med.

408. Valid Word Abbreviation
36.5%
Easy

415. Add Strings
51.7%
Easy

498. Diagonal Traverse
62.1%
Med.

523. Continuous Subarray Sum
30.6%
Med.

543. Diameter of Binary Tree
62.4%
Easy

560. Subarray Sum Equals K
44.7%
Med.

1539. Kth Missing Positive Number
61.5%
Easy

636. Exclusive Time of Functions
63.7%
Med.

647. Palindromic Substrings
71.1%
Med.

658. Find K Closest Elements
48.2%
Med.

670. Maximum Swap
51.7%
Med.

680. Valid Palindrome II
42.2%
Easy

1570. Dot Product of Two Sparse Vectors
89.9%
Med.

691. Stickers to Spell Word
49.8%
Hard

721. Accounts Merge
58.6%
Med.

426. Convert Binary Search Tree to Sorted Doubly Linked List
65.3%
Med.

2667. Create Hello World Function
81.8%
Easy

1650. Lowest Common Ancestor of a Binary Tree III
81.6%
Med.

766. Toeplitz Matrix
69.4%
Easy

791. Custom Sort String
71.5%
Med.

708. Insert into a Sorted Circular Linked List
37.4%
Med.

827. Making A Large Island
49.7%
Hard

1768. Merge Strings Alternately
81.6%
Easy

1757. Recyclable and Low Fat Products
89.4%
Easy

1762. Buildings With an Ocean View
80.4%
Med.

528. Random Pick with Weight
48.0%
Med.

921. Minimum Add to Make Parentheses Valid
74.7%
Med.

938. Range Sum of BST
87.3%
Easy

1868. Product of Two Run-Length Encoded Arrays
59.1%
Med.

973. K Closest Points to Origin
67.4%
Med.

977. Squares of a Sorted Array
73.0%
Easy

16. 3Sum Closest
46.4%
Med.

25. Reverse Nodes in k-Group
61.6%
Hard

76. Minimum Window Substring
44.4%
Hard

91. Decode Ways
35.9%
Med.

206. Reverse Linked List
78.4%
Easy

273. Integer to English Words
34.2%
Hard

286. Walls and Gates
62.4%
Med.

824. Goat Latin
68.9%
Easy

394. Decode String
60.5%
Med.

1778. Shortest Path in a Hidden Grid
43.3%
Med.

796. Rotate String
63.4%
Easy

231. Power of Two
48.1%
Easy

19. Remove Nth Node From End of List
47.7%
Med.

197. Rising Temperature
49.6%
Easy

450. Delete Node in a BST
52.4%
Med.

1424. Diagonal Traverse II
57.5%
Med.

875. Koko Eating Bananas
48.7%
Med.

863. All Nodes Distance K in Binary Tree
65.6%
Med.

934. Shortest Bridge
58.2%
Med.

419. Battleships in a Board
76.1%
Med.

163. Missing Ranges
34.8%
Easy

249. Group Shifted Strings
66.7%
Med.

179. Largest Number
40.6%
Med.

443. String Compression
56.9%
Med.

392. Is Subsequence
48.2%
Easy

46. Permutations
79.9%
Med.

386. Lexicographical Numbers
72.9%
Med.

1047. Remove All Adjacent Duplicates In String
70.8%
Easy

329. Longest Increasing Path in a Matrix
54.7%
Hard

54. Spiral Matrix
52.5%
Med.

328. Odd Even Linked List
61.8%
Med.

81. Search in Rotated Sorted Array II
38.5%
Med.

246. Strobogrammatic Number
47.6%
Easy

104. Maximum Depth of Binary Tree
76.6%
Easy

143. Reorder List
61.2%
Med.

27. Remove Element
59.1%
Easy

136. Single Number
75.0%
Easy

63. Unique Paths II
42.6%
Med.

198. House Robber
51.9%
Med.

22. Generate Parentheses
76.2%
Med.

695. Max Area of Island
72.8%
Med.

116. Populating Next Right Pointers in Each Node
64.5%
Med.

103. Binary Tree Zigzag Level Order Traversal
60.7%
Med.

151. Reverse Words in a String
49.1%
Med.

383. Ransom Note
63.6%
Easy

378. Kth Smallest Element in a Sorted Matrix
63.1%
Med.

295. Find Median from Data Stream
52.8%
Hard

536. Construct Binary Tree from String
57.8%
Med.

767. Reorganize String
55.6%
Med.

21. Merge Two Sorted Lists
66.0%
Easy

2090. K Radius Subarray Averages
46.0%
Med.

29. Divide Two Integers
18.0%
Med.

224. Basic Calculator
44.5%
Hard

66. Plus One
46.8%
Easy

1110. Delete Nodes And Return Forest
72.5%
Med.

114. Flatten Binary Tree to Linked List
67.3%
Med.

131. Palindrome Partitioning
71.1%
Med.

1233. Remove Sub-Folders from the Filesystem
75.6%
Med.

704. Binary Search
59.0%
Easy

94. Binary Tree Inorder Traversal
77.8%
Easy

230. Kth Smallest Element in a BST
74.4%
Med.

490. The Maze
59.0%
Med.

239. Sliding Window Maximum
47.1%
Hard

1891. Cutting Ribbons
51.4%
Med.

825. Friends Of Appropriate Ages
48.7%
Med.

509. Fibonacci Number
72.3%
Easy

234. Palindrome Linked List
54.9%
Easy

958. Check Completeness of a Binary Tree
57.8%
Med.

229. Majority Element II
53.4%
Med.

494. Target Sum
50.1%
Med.

1197. Minimum Knight Moves
41.1%
Med.

735. Asteroid Collision
45.0%
Med.

814. Binary Tree Pruning
72.3%
Med.

109. Convert Sorted List to Binary Search Tree
63.6%
Med.

303. Range Sum Query - Immutable
66.7%
Easy

122. Best Time to Buy and Sell Stock II
68.5%
Med.

287. Find the Duplicate Number
62.1%
Med.

983. Minimum Cost For Tickets
67.4%
Med.

435. Non-overlapping Intervals
54.7%
Med.

325. Maximum Size Subarray Sum Equals k
50.1%
Med.

1498. Number of Subsequences That Satisfy the Given Sum Condition
43.8%
Med.

62. Unique Paths
65.2%
Med.

1280. Students and Examinations
60.0%
Easy

1644. Lowest Common Ancestor of a Binary Tree II
67.7%
Med.

605. Can Place Flowers
28.8%
Easy

545. Boundary of Binary Tree
46.6%
Med.

266. Palindrome Permutation
68.0%
Easy

2235. Add Two Integers
88.1%
Easy

79. Word Search
44.3%
Med.

616. Add Bold Tag in String
50.7%
Med.

252. Meeting Rooms
58.7%
Easy

787. Cheapest Flights Within K Stops
39.9%
Med.

202. Happy Number
57.4%
Easy

529. Minesweeper
67.6%
Med.

40. Combination Sum II
57.0%
Med.

1275. Find Winner on a Tic Tac Toe Game
54.0%
Easy

2914. Minimum Number of Changes to Make Binary String Beautiful
77.0%
Med.

1493. Longest Subarray of 1's After Deleting One Element
68.5%
Med.

169. Majority Element
65.4%
Easy

876. Middle of the Linked List
79.9%
Easy

126. Word Ladder II
27.1%
Hard

67. Add Binary
55.0%
Easy

296. Best Meeting Point
61.1%
Hard

12. Integer to Roman
67.4%
Med.

242. Valid Anagram
65.9%
Easy

862. Shortest Subarray with Sum at Least K
32.2%
Hard

3097. Shortest Subarray With OR at Least K II
50.5%
Med.

117. Populating Next Right Pointers in Each Node II
54.5%
Med.

73. Set Matrix Zeroes
58.5%
Med.

489. Robot Room Cleaner
77.1%
Hard

703. Kth Largest Element in a Stream
59.6%
Easy

643. Maximum Average Subarray I
44.4%
Easy

1845. Seat Reservation Manager
69.9%
Med.

451. Sort Characters By Frequency
73.5%
Med.

852. Peak Index in a Mountain Array
67.9%
Med.

1382. Balance a Binary Search Tree
84.7%
Med.

2303. Calculate Amount Paid in Taxes
66.7%
Easy

2427. Number of Common Factors
79.4%
Easy

1652. Defuse the Bomb
79.3%
Easy

723. Candy Crush
77.1%
Med.

35. Search Insert Position
48.0%
Easy

1161. Maximum Level Sum of a Binary Tree
67.2%
Med.

217. Contains Duplicate
62.6%
Easy

773. Sliding Puzzle
72.9%
Hard

77. Combinations
72.0%
Med.

907. Sum of Subarray Minimums
37.3%
Med.

501. Find Mode in Binary Search Tree
57.0%
Easy

101. Symmetric Tree
58.3%
Easy

678. Valid Parenthesis String
38.5%
Med.

1443. Minimum Time to Collect All Apples in a Tree
62.7%
Med.

247. Strobogrammatic Number II
52.8%
Med.

1581. Customer Who Visited but Did Not Make Any Transactions
67.7%
Easy

167. Two Sum II - Input Array Is Sorted
62.6%
Med.

2109. Adding Spaces to a String
71.7%
Med.

1060. Missing Element in Sorted Array
58.0%
Med.

1029. Two City Scheduling
67.3%
Med.

2034. Stock Price Fluctuation
48.6%
Med.

258. Add Digits
67.5%
Easy

1679. Max Number of K-Sum Pairs
55.7%
Med.

865. Smallest Subtree with all the Deepest Nodes
71.4%
Med.

1346. Check If N and Its Double Exist
41.0%
Easy

2337. Move Pieces to Obtain a String
57.1%
Med.

1331. Rank Transform of an Array
70.6%
Easy

507. Perfect Number
43.5%
Easy

100. Same Tree
64.2%
Easy

13. Roman to Integer
63.8%
Easy

36. Valid Sudoku
61.4%
Med.

689. Maximum Sum of 3 Non-Overlapping Subarrays
59.3%
Hard

210. Course Schedule II
52.3%
Med.

395. Longest Substring with At Least K Repeating Characters
45.3%
Med.

2981. Find Longest Special Substring That Occurs Thrice I
62.3%
Med.

176. Second Highest Salary
42.6%
Med.

2558. Take Gifts From the Richest Pile
75.8%
Easy

84. Largest Rectangle in Histogram
46.3%
Hard

2593. Find Score of an Array After Marking All Elements
65.0%
Med.

1431. Kids With the Greatest Number of Candies
87.9%
Easy

912. Sort an Array
57.3%
Med.

6. Zigzag Conversion
50.4%
Med.

2125. Number of Laser Beams in a Bank
85.5%
Med.

28. Find the Index of the First Occurrence in a String
44.2%
Easy

222. Count Complete Tree Nodes
68.5%
Easy

1277. Count Square Submatrices with All Ones
78.5%
Med.

412. Fizz Buzz
73.7%
Easy

98. Validate Binary Search Tree
33.8%
Med.

541. Reverse String II
51.5%
Easy

1094. Car Pooling
56.0%
Med.

1287. Element Appearing More Than 25% In Sorted Array
61.0%
Easy

2704. To Be Or Not To Be
62.6%
Easy

2352. Equal Row and Column Pairs
70.3%
Med.

18. 4Sum
37.3%
Med.

515. Find Largest Value in Each Tree Row
66.4%
Med.

696. Count Binary Substrings
65.8%
Easy

595. Big Countries
68.2%
Easy

268. Missing Number
69.0%
Easy

1014. Best Sightseeing Pair
62.6%
Med.

496. Next Greater Element I
73.7%
Easy

193. Valid Phone Numbers
26.8%
Easy

1639. Number of Ways to Form a Target String Given a Dictionary
57.4%
Hard

305. Number of Islands II
40.0%
Hard

417. Pacific Atlantic Water Flow
56.7%
Med.

2466. Count Ways To Build Good Strings
59.3%
Med.

416. Partition Equal Subset Sum
47.1%
Med.

1422. Maximum Score After Splitting a String
65.2%
Easy

1378. Replace Employee ID With The Unique Identifier
83.7%
Easy

160. Intersection of Two Linked Lists
59.9%
Easy

1358. Number of Substrings Containing All Three Characters
68.5%
Med.

2270. Number of Ways to Split Array
56.2%
Med.

1903. Largest Odd Number in String
64.3%
Easy

1930. Unique Length-3 Palindromic Subsequences
70.8%
Med.

2381. Shifting Letters II
53.1%
Med.

130. Surrounded Regions
41.7%
Med.

448. Find All Numbers Disappeared in an Array
61.8%
Easy

1011. Capacity To Ship Packages Within D Days
71.1%
Med.

1769. Minimum Number of Operations to Move All Balls to Each Box
90.2%
Med.

918. Maximum Sum Circular Subarray
46.6%
Med.

1944. Number of Visible People in a Queue
70.3%
Hard

152. Maximum Product Subarray
34.4%
Med.

189. Rotate Array
42.2%
Med.

393. UTF-8 Validation
45.3%
Med.

402. Remove K Digits
34.3%
Med.

2185. Counting Words With a Given Prefix
84.6%
Easy

916. Word Subsets
55.5%
Med.

1400. Construct K Palindrome Strings
68.8%
Med.

1245. Tree Diameter
61.1%
Med.

155. Min Stack
55.6%
Med.

2116. Check if a Parentheses String Can Be Valid
44.7%
Med.

297. Serialize and Deserialize Binary Tree
58.1%
Hard

2265. Count Nodes Equal to Average of Subtree
86.5%
Med.

2348. Number of Zero-Filled Subarrays
66.7%
Med.

2657. Find the Prefix Common Array of Two Arrays
87.7%
Med.

771. Jewels and Stones
89.0%
Easy

772. Basic Calculator III
51.7%
Hard

530. Minimum Absolute Difference in BST
58.6%
Easy

344. Reverse String
79.4%
Easy

2013. Detect Squares
51.6%
Med.

149. Max Points on a Line
28.2%
Hard

424. Longest Repeating Character Replacement
56.1%
Med.

74. Search a 2D Matrix
51.6%
Med.

1748. Sum of Unique Elements
78.6%
Easy

381. Insert Delete GetRandom O(1) - Duplicates allowed
35.7%
Hard

1368. Minimum Cost to Make at Least One Valid Path in a Grid
70.8%
Hard

1123. Lowest Common Ancestor of Deepest Leaves
73.0%
Med.

407. Trapping Rain Water II
58.5%
Hard

739. Daily Temperatures
66.8%
Med.

388. Longest Absolute File Path
48.0%
Med.

692. Top K Frequent Words
58.8%
Med.

3161. Block Placement Queries
15.5%
Hard

92. Reverse Linked List II
48.9%
Med.

3428. Maximum and Minimum Sums of at Most Size K Subsequences
18.8%
Med.

205. Isomorphic Strings
46.2%
Easy

584. Find Customer Referee
71.4%
Easy

141. Linked List Cycle
51.7%
Easy

2620. Counter
81.9%
Easy

61. Rotate List
39.2%
Med.

802. Find Eventual Safe States
66.5%
Med.

655. Print Binary Tree
65.1%
Med.

