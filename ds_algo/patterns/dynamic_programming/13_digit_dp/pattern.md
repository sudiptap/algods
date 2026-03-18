# Digit DP

## Core Idea
Count numbers up to N satisfying some digit constraint. Process digit by digit, tracking whether we're still "tight" (bounded by N).

## Template
```python
from functools import lru_cache

def count_up_to(num_str):
    @lru_cache(maxsize=None)
    def dp(pos, tight, state):
        if pos == len(num_str):
            return 1 if valid(state) else 0
        limit = int(num_str[pos]) if tight else 9
        result = 0
        for digit in range(0, limit + 1):
            new_tight = tight and (digit == limit)
            new_state = transition(state, digit)
            result += dp(pos + 1, new_tight, new_state)
        return result

    return dp(0, True, initial_state)
```

## Complexity
- Time: O(digits * states * 10)
- Space: O(digits * states)

## Classic Problems
- 233. Number of Digit One
- 902. Numbers At Most N Given Digit Set
- 1012. Numbers With Repeated Digits
- 2376. Count Special Integers
