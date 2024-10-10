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

### Pattern 9 - LC 560, 930
```
```

## ------ Meta Tagged ------
### Standard Sliding window LC 1004
```
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        zeros = 0
        mx = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            mx = max(mx, right - left + 1)
            right += 1
        return mx
        
```
### Sliding window median
```
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # I was confused by the official solution and many of the top posts. This problem shouldn't be that hard! I ended up using the same template as in Question 295 and passed all tests on my first attempt. The key is using two heaps (just like 295) and keeping track of just two things - the element to include and the element to remove. Below is my Python solution:

        if not nums or not k:
            return []
        lo = [] # max heap
        hi = [] # min heap
        for i in range(k):
            if len(lo) == len(hi):
                heapq.heappush(hi, -heapq.heappushpop(lo, -nums[i]))
            else:
                heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))
        ans = [float(hi[0])] if k & 1 else [(hi[0] - lo[0]) / 2.0]
        to_remove = defaultdict(int)
        for i in range(k, len(nums)): # right bound of window
            heapq.heappush(lo, -heapq.heappushpop(hi, nums[i])) # always push to lo
            out_num = nums[i-k]
            if out_num > -lo[0]:
                heapq.heappush(hi, -heapq.heappop(lo))
            to_remove[out_num] += 1
            while lo and to_remove[-lo[0]]:
                to_remove[-lo[0]] -= 1
                heapq.heappop(lo)
            while to_remove[hi[0]]:
                to_remove[hi[0]] -= 1
                heapq.heappop(hi)
            if k % 2:
                ans.append(float(hi[0]))
            else:
                ans.append((hi[0] - lo[0]) / 2.0)
        return ans
# A few important things to clarify:

# Two heaps (lo and hi). The size of hi, as measured by the number of valid elements it contains, is either equal to that of lo or one greater than that of lo, depending on the value of k. (This is an invariant we enforce when we add and remove elements from lo and hi). It's worth noting that by "valid" I mean elements within the current window.
# Lazy removal. I used a defaultdict to_remove to keep track of elements to be removed and their occurrances, and remove them if and only if they are at the top of either heaps.
# How to add and remove. The logic is extremely straightforward. When adding a new element, we always add to lo. If the element to be removed is in lo as well, great! We don't need to do anything because the heap sizes do not change. However, if the element to be removed happen to be in hi, we then pop an element from lo and add it to hi. Important: that element we pop is guaranteed be a valid element(!!) because otherwise it should have been removed during the previous iteration.
# Some may be worried that removing elements makes heaps imbalanced. That never happens! No matter how many elements are removed at the end of an iteration, they are invalid elements! The heap lo can contain all the invalid elements and much greater in size than hi, but still in perfect balance with hi. As long as lo and hi each contains half (or (half, half+1) when k is odd) of the elements in the current window, we say that they are balanced.

```

## LC 658 - k closest element
```
What is the idea: Here we are looking for the best interval using binary search, since we are looking for interval of size k, so binary search low and high are set to 0 and len(arr)-k
question would be given an interval [i:i+k] how do we decide if we need to shift left to [i-1:i+k-1] or right [i+1: i+k+1] . if x - arr[i] > arr[i+k] - x then by moving right we have better candidate
for finding closest elements and viceversa. 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, h = 0, len(arr)-k
        while l<h:
            mid = (l+h)//2
            if x - arr[mid] > arr[mid+k] - x:
                l = mid + 1
            else:
                h = mid
        return arr[l:l+k]
```

## LC 219
```
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left, right = 0, 0
        while right < len(nums):
            if right -left > k:
                # we have invalid window
                # remove left from window and
                # increase left
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
            right += 1
        return False
```

## LC 727
```

```

## LC 713
```
Trick: This is a standard sliding window with the following trick, The count of subarrays ending at j starting at i = j - i + 1
```

## LC 424
```
Idea: for any window how do we know if the current window is valid? we need to make a decision wheather we should do right+= 1 or left += 1
we will keep freq of chars in the window and check if len(window) - max(freq) > k, if so then we ran out of k to replace the others chars to most frequent char
to convert the substring into all same chars. Hence we shrink the window by doing left += 1


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0
        
        left = 0
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            #window_size = right - left + 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            res = max(res, (right - left + 1))
        return res
```

## Practice:
### LC2461
### LC424

3. Longest Substring Without Repeating Characters
35.5%
Medium
1358. Number of Substrings Containing All Three Characters
68.0%
Medium
995. Minimum Number of K Consecutive Bit Flips
62.7%
Hard
340. Longest Substring with At Most K Distinct Characters
49.1%
Medium
2962. Count Subarrays Where Max Element Appears at Least K Times
58.9%
Medium
239. Sliding Window Maximum
46.9%
Hard
930. Binary Subarrays With Sum
64.0%
Medium
1052. Grumpy Bookstore Owner
64.2%
Medium
643. Maximum Average Subarray I
44.0%
Easy
438. Find All Anagrams in a String
51.4%
Medium
1838. Frequency of the Most Frequent Element
44.1%
Medium
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
56.6%
Medium
209. Minimum Size Subarray Sum
48.0%
Medium
992. Subarrays with K Different Integers
64.3%
Hard
567. Permutation in String
46.3%
Medium