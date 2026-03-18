# State Machine DP

## Core Idea
Model the problem as transitions between discrete states. At each step, transition based on the current input.

## Template (Buy/Sell Stock with cooldown)
```python
def max_profit(prices):
    # States: held, sold, rest
    held = float('-inf')
    sold = 0
    rest = 0
    for price in prices:
        prev_held = held
        held = max(held, rest - price)    # buy
        rest = max(rest, sold)            # cooldown
        sold = prev_held + price          # sell
    return max(sold, rest)
```

## Complexity
- Time: O(n * states)
- Space: O(states) with compression

## Classic Problems
- 121/122/123/188/309/714. Best Time to Buy and Sell Stock (I-VI)
- 552. Student Attendance Record II
- 801. Minimum Swaps To Make Sequences Increasing
- 256. Paint House
