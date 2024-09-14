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
```

### Next smaller to left and right
#### Sum of subarray minimums - LC 907
```
```

### Implement Q using stacks
#### LC 232
```
```