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
#### kth missing number
```

```

#### Binary search on the ans
minimize max or max min is a pattern for this
```
LC-2439
LC-2968 (LC hard practice)

```
#### Median of two sorted arrays
```
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
