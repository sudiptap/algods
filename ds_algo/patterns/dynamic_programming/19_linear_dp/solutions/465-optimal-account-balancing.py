"""
465. Optimal Account Balancing (Hard)
https://leetcode.com/problems/optimal-account-balancing/

Pattern: Linear DP / Backtracking

Given a list of transactions [from, to, amount], find the minimum
number of transactions to settle all debts.

Approach:
    1. Compute net balance for each person.
    2. Filter out zero balances.
    3. Backtracking: try to settle debt[i] with each debt[j] where
       j > i and debt[j] has opposite sign. Settle debt[i] into debt[j],
       recurse on i+1, then undo. Track minimum transactions.
    Pruning: if debt[i] + debt[j] == 0, this pair perfectly cancels;
    no need to try other options for debt[i].

Time:  O(n!) worst case, but heavy pruning makes it practical
Space: O(n) for recursion
"""

from collections import defaultdict
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """Return minimum number of transactions to settle all debts."""
        balance = defaultdict(int)
        for a, b, amt in transactions:
            balance[a] -= amt
            balance[b] += amt

        debts = [v for v in balance.values() if v != 0]

        def backtrack(idx: int) -> int:
            while idx < len(debts) and debts[idx] == 0:
                idx += 1
            if idx == len(debts):
                return 0

            best = float("inf")
            seen = set()
            for j in range(idx + 1, len(debts)):
                if debts[j] * debts[idx] < 0 and debts[j] not in seen:
                    seen.add(debts[j])
                    debts[j] += debts[idx]
                    best = min(best, 1 + backtrack(idx + 1))
                    debts[j] -= debts[idx]
                    if debts[j] + debts[idx] == 0:
                        break  # perfect match, no need to try others
            return best

        return backtrack(0)


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().minTransfers([[0,1,10],[2,0,5]]) == 2

def test_example2():
    assert Solution().minTransfers([[0,1,10],[1,0,1],[1,2,5],[2,0,5]]) == 1

def test_no_transactions():
    assert Solution().minTransfers([]) == 0

def test_already_balanced():
    assert Solution().minTransfers([[0,1,10],[1,0,10]]) == 0

def test_three_way():
    # 0->1: 5, 1->2: 5 => net: 0:-5, 1:0, 2:5 => 1 transaction
    assert Solution().minTransfers([[0,1,5],[1,2,5]]) == 1

def test_complex():
    assert Solution().minTransfers([[0,1,2],[1,2,1],[1,3,1]]) == 2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
