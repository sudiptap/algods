"""
964. Least Operators to Express Number (Hard)
https://leetcode.com/problems/least-operators-to-express-number/

Given a positive integer x and target, express target using only x with
operators +, -, *, / (no parentheses, standard precedence). Return minimum
number of operators.

Key insight: The expression is a sequence of x-symbols separated by operators.
Total operators = (total x-symbols used) - 1. We represent target as a
sum/difference of multiples of powers of x, minimizing total x-symbols.

Pattern: Linear DP / Memoized Recursion
Approach:
- Express target in base x, process digit by digit.
- At each position i with digit d, either:
  (A) Use d copies of x^i (cost d * tokens(i) x-symbols), or
  (B) Round up: subtract (x-d) copies of x^i and carry 1 to next position.
- tokens(i) = 2 if i==0 else i  (x/x needs 2 symbols, x^i needs i symbols).
- Base case for the carry path: when carry propagates past the highest digit,
  just use 1 copy of x^(highest+1).

Time:  O(log_x(target))
Space: O(log_x(target))
"""

from functools import lru_cache
import math


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """Return minimum operators to express target using x.

        Args:
            x: Base integer, 2 <= x <= 100.
            target: Target value, 1 <= target <= 2*10^8.

        Returns:
            Minimum number of operators.
        """
        # Precompute digits of target in base x
        digits = []
        t = target
        while t > 0:
            digits.append(t % x)
            t //= x
        # digits[i] = digit at position i (x^i)

        n = len(digits)

        # Process from least significant to most significant digit.
        # At each position, decide: use digit as-is, or round up (carry to next).
        # Track two costs:
        #   cost_no_carry: best cost if we DON'T carry into position i+1
        #   cost_carry: best cost if we DO carry 1 into position i+1

        cost_no_carry = 0
        cost_carry = float('inf')  # no carry initially

        for i in range(n):
            d = digits[i]
            tokens_i = 2 if i == 0 else i  # x-symbols per copy of x^i

            # If there's no carry from previous position:
            # Option A (no carry forward): use d copies -> d * tokens_i
            # Option B (carry forward): use (x - d) copies subtracted -> (x - d) * tokens_i
            a_no = cost_no_carry + d * tokens_i
            b_no = cost_no_carry + (x - d) * tokens_i

            # If there IS a carry from previous position (digit becomes d+1):
            # Option A (no carry forward): use (d+1) copies -> (d+1) * tokens_i
            # Option B (carry forward): use (x - d - 1) copies subtracted -> (x - d - 1) * tokens_i
            a_carry = cost_carry + (d + 1) * tokens_i
            b_carry = cost_carry + (x - d - 1) * tokens_i

            cost_no_carry = min(a_no, a_carry)
            cost_carry = min(b_no, b_carry)

        # After processing all digits:
        # If we carry, we need one more x^n which costs n x-symbols (or n+1... let me think)
        # x^n requires n x-symbols (x * x * ... * x, n times, n-1 multiplications)
        # But wait, n here is the number of digits. x^n means n+1... no.
        # Actually, x^i uses i copies of x with i-1 multiplications.
        # Wait: x^0 = x/x = 2 x-symbols. x^1 = x = 1 x-symbol. x^2 = x*x = 2 x-symbols.
        # x^i = i x-symbols for i >= 1, 2 x-symbols for i = 0.
        # Hmm, that means x^1 uses 1 x-symbol. But to combine it with other terms we need operators.
        # Total operators = total x-symbols - 1 for the whole expression.
        #
        # So for the carry case: we need 1 copy of x^n, costing n x-symbols (since n >= 1).
        cost_carry += n  # 1 copy of x^n = n x-symbols

        return min(cost_no_carry, cost_carry) - 1


# ---------- tests ----------
def test_least_ops_express_target():
    sol = Solution()

    # Example 1: x=3, target=19 = 201 in base 3
    # 2*9 + 0*3 + 1*1 -> x*x+x*x+x/x = 6 x-symbols, 5 operators
    assert sol.leastOpsExpressTarget(3, 19) == 5

    # Example 2: x=5, target=501 -> 8 operators
    assert sol.leastOpsExpressTarget(5, 501) == 8

    # Example 3: x=100, target=100000000 = 100^4 -> 4 x-symbols, 3 operators
    assert sol.leastOpsExpressTarget(100, 100000000) == 3

    # x=2, target=1 -> 2/2 = 2 x-symbols, 1 operator
    assert sol.leastOpsExpressTarget(2, 1) == 1

    # x=3, target=3 -> just "3" = 1 x-symbol, 0 operators
    assert sol.leastOpsExpressTarget(3, 3) == 0

    print("All tests passed for 964. Least Operators to Express Number")


if __name__ == "__main__":
    test_least_ops_express_target()
