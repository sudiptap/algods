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
def upper_bound(nums, target):
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
            if nums[mid] < target <= nums[high] :
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
#### find min in rotated sorted array
```
def find_min(nums, target):
    low, high = 0, len(nums)-1
    while low < high:
        mid = (low + high)//2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return low
```

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
#### kth missing positive number LC 1539
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

#### Binary search on the ans
minimize max or max min is a pattern for this
```
LC-2439
LC-2968 (LC hard practice)

```
#### Median of two sorted arrays
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

####  Nexted binary search 
```
LC 1608
```

### LC for practice
```
LC-2968
LC -1608
```
### Missing element in sorted array
```
LC 1060
# when nums = [4,7,9,10], there is a missed_element_array = [0, 2, 3, 3],
# So before nums[i] = 7, there exist 2 missed element(5,6), before nums[i] = 9, there exist 3 missed element(5,6,8).
# Therefore the equation we use to count the missed number should be num[i] - num[0] - i

# First, we should find the first num[i] that have greater missing element than k by using binary search.
# In nums = [4,7,9,10], if k = 1, then num[i] should be 7.

# so the k number is between range of 4 - 7,
# num[k] = nums[i-1] + (k - (nums[i-1] - nums[0] - (i-1)))
# 4 + k - (missed element for 4)
# we can get 4 + (1 - 0) = 5

class Solution:
	def missingElement(self, nums: List[int], k: int) -> int:
		
		l = 0
		r = len(nums)

		while l < r:
			mid = (l + r) // 2

			if nums[mid] - nums[0] - mid < k:
				l = mid + 1
			else:
				r = mid


		return nums[l-1] + (k - (nums[l-1] - nums[0] - (l-1)))
        
```
### 658. Find K Closest Elements
```
Tirck is to use binary search to search for a valid window 
```

### 378 Kth smallest element in sorted matrix
```
class Solution:  # 160 ms, faster than 93.06%
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: c -= 1  # decrease column until matrix[r][c] <= x
                cnt += (c + 1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1  # try to looking for a smaller value in the left side
            else:
                left = mid + 1  # try to looking for a bigger value in the right side

        return ans
```

### 1439 - very imp
```
Logic - this is a heap question, Try the following way, get a min heap that stores [sum, indices] but ordered by the sum. smallest sum would be all 0th elements. then increase index of each array by 1 while keeping other indices of other arrays fixed and calculate the sum again, for these newly calculated sum push them into the heap. Do this till we find k elements.
```

### Sqrt x 69
```
```
### 1428 left column with atleast a one
```
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        num_rows, num_cols = binaryMatrix.dimensions()
        row = 0
        col = num_cols-1
        while row <= num_rows-1 and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                col -= 1
            else:
                row +=1
        if col == num_cols-1:
            return -1
        else:
            return col+1
```

### Search in 2D matrix
```
Double binary search
```

### LC1838
```
https://www.youtube.com/watch?v=vgBrQ0NM5vE&t=613s
https://www.youtube.com/watch?v=iOqH_JnXIOQ 
```

## Practice
1891
1213 - asked me in meta interview
1439
2468
633
1428
3186
1838 - sliding winodw 