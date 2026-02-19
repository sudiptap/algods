# Intervals

## When to Use
- Problems involving **ranges, time slots, or intervals**
- Merging, inserting, or finding overlaps
- Keywords: "intervals", "overlap", "merge", "meeting rooms", "schedule"

## Core Idea
Sort intervals by start time. Then process them left to right, tracking the current interval's end.

## Key Insight: Overlap Detection
Two intervals `[a, b]` and `[c, d]` overlap if and only if `a < d and c < b`.

## Templates

### Merge Intervals
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### Insert Interval
```python
def insert(intervals, new):
    result = []
    for i, (start, end) in enumerate(intervals):
        if end < new[0]:
            result.append([start, end])
        elif start > new[1]:
            result.append(new)
            return result + intervals[i:]
        else:
            new = [min(start, new[0]), max(end, new[1])]
    result.append(new)
    return result
```

### Meeting Rooms (Min Rooms Needed)
```python
import heapq

def min_meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []  # end times
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)
```

## Complexity
- Time: O(n log n) due to sorting
- Space: O(n)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 56 | Merge Intervals | Medium | Merge | |
| 57 | Insert Interval | Medium | Insert | |
| 252 | Meeting Rooms | Easy | Overlap check | |
| 253 | Meeting Rooms II | Medium | Min rooms | |
| 435 | Non-overlapping Intervals | Medium | Greedy removal | |
| 452 | Minimum Number of Arrows | Medium | Greedy | |
| 986 | Interval List Intersections | Medium | Two pointers | |
| 1288 | Remove Covered Intervals | Medium | Sort + scan | |

## Tips
- Almost always start by sorting by start time
- For "minimum rooms" or "maximum overlap", think about a min-heap of end times
- Sweep line is an advanced technique for complex interval problems
