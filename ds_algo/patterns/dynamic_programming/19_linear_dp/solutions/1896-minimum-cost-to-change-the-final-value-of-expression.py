"""
1896. Minimum Cost to Change the Final Value of Expression (Hard)
https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

Given a valid boolean expression with '0', '1', '&', '|', '(', ')',
return the minimum cost (number of operations) to change its value.
Operations: flip a value, change & to | or | to &.

Pattern: Linear DP / Expression Parsing
Approach:
- Parse the expression into an expression tree using a stack.
- For each subexpression, compute (value, min_cost_to_flip).
- For a leaf '0': value=0, cost_to_flip=1.
- For a leaf '1': value=1, cost_to_flip=1.
- For (left op right):
  - If op='&':
    - val = left_val & right_val
    - To flip from 1->0: min(lc, rc) (flip either to 0)
    - To flip from 0->0 with both 0: min(lc+rc, change_op_cost)
      where change_op_cost = flip to | = 1 + min(lc, rc)...
  Let lv, lc = left value, left flip cost. rv, rc = right.
  If op = '&':
    if lv==1 and rv==1: val=1, flip_cost=min(lc, rc)
    if lv==1 and rv==0: val=0, flip_cost=min(lc+rc, 1+rc)...
    Actually cleaner:
    val = lv & rv
    To flip to 1 (from 0):
      - keep &: both must be 1: need to flip the 0s
      - change to |: cost 1 + at least one must be 1
    To flip to 0 (from 1):
      - keep &: at least one must be 0: min cost to flip one
      - change to |: both must be 0: need to flip both
  Similarly for '|'.

Time:  O(n)
Space: O(n)
"""


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        """Return min ops to change the expression's final value.

        Args:
            expression: Valid boolean expression string.

        Returns:
            Minimum number of operations.
        """
        # Stack-based parsing
        # Each element on stack: (value, cost_to_flip) or an operator
        stack = []
        ops = []  # operator stack

        def combine(left, op, right):
            lv, lc = left
            rv, rc = right
            if op == '&':
                val = lv & rv
                if val == 1:
                    # Both are 1, flip either to 0 (keep &), or change to | (still 1)
                    flip_cost = min(lc, rc)
                else:
                    # val == 0
                    if lv == 0 and rv == 0:
                        # Keep &: flip both to 1: lc + rc
                        # Change to |: flip one to 1: 1 + min(lc, rc)
                        flip_cost = 1 + min(lc, rc)
                    elif lv == 0 and rv == 1:
                        # Keep &: flip lv to 1: lc
                        # Change to |: cost 1 (rv already 1)
                        flip_cost = min(lc, 1)
                    else:  # lv == 1, rv == 0
                        flip_cost = min(rc, 1)
            else:  # op == '|'
                val = lv | rv
                if val == 0:
                    # Both are 0, flip either to 1
                    flip_cost = min(lc, rc)
                else:
                    # val == 1
                    if lv == 1 and rv == 1:
                        # Keep |: flip both to 0: lc + rc
                        # Change to &: flip one to 0: 1 + min(lc, rc)
                        flip_cost = 1 + min(lc, rc)
                    elif lv == 1 and rv == 0:
                        # Keep |: flip lv to 0: lc
                        # Change to &: cost 1 (rv already 0)
                        flip_cost = min(lc, 1)
                    else:  # lv == 0, rv == 1
                        flip_cost = min(rc, 1)
            return (val, flip_cost)

        for ch in expression:
            if ch == '(':
                stack.append('(')
                ops.append('(')
            elif ch == ')':
                ops.pop()  # remove '('
                # top of stack has the result inside parens
                # if there was an operator before '(', combine
                if ops and ops[-1] != '(':
                    op = ops.pop()
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(combine(left, op, right))
            elif ch in '&|':
                ops.append(ch)
            else:  # '0' or '1'
                val = int(ch)
                stack.append((val, 1))
                # Check if we can combine with previous
                if ops and ops[-1] in '&|':
                    op = ops.pop()
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(combine(left, op, right))

        return stack[0][1]


# ---------- tests ----------
def test_min_ops_to_flip():
    sol = Solution()

    # Example 1: "1&(0|1)" evaluates to 1, cost to flip = 1
    assert sol.minOperationsToFlip("1&(0|1)") == 1

    # Example 2: "(0&0)&(0&0&0)" evaluates to 0, cost = 3
    assert sol.minOperationsToFlip("(0&0)&(0&0&0)") == 3

    # Example 3: "(0|(1|0&1))" evaluates to 1, cost = 1
    assert sol.minOperationsToFlip("(0|(1|0&1))") == 1

    # Simple: "0" -> cost 1
    assert sol.minOperationsToFlip("0") == 1

    # Simple: "1" -> cost 1
    assert sol.minOperationsToFlip("1") == 1

    print("All tests passed for 1896. Minimum Cost to Change Final Value of Expression")


if __name__ == "__main__":
    test_min_ops_to_flip()
