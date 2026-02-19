# Fast & Slow Pointers (Floyd's Tortoise and Hare)

## When to Use
- **Cycle detection** in linked lists or arrays
- Finding the **middle** of a linked list
- Finding the **start of a cycle**
- Keywords: "cycle", "circular", "middle", "linked list"

## Core Idea
Move two pointers at different speeds. The fast pointer moves 2 steps, the slow pointer moves 1 step. If there's a cycle, they'll meet.

## Templates

### Cycle Detection
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Find Cycle Start
```python
def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Reset one pointer to head
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # cycle start
    return None
```

### Find Middle of Linked List
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # middle node
```

## Complexity
- Time: O(n)
- Space: O(1)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 141 | Linked List Cycle | Easy | Detection | |
| 142 | Linked List Cycle II | Medium | Find Start | |
| 143 | Reorder List | Medium | Find Middle | |
| 202 | Happy Number | Easy | Cycle Detection | |
| 234 | Palindrome Linked List | Easy | Find Middle | |
| 287 | Find the Duplicate Number | Medium | Cycle in Array | |
| 876 | Middle of the Linked List | Easy | Find Middle | |

## Tips
- For "find middle": when fast reaches end, slow is at middle
- The math behind cycle start detection: distance from head to cycle start equals distance from meeting point to cycle start
