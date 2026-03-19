"""
3857. Minimum Cost to Split into Ones
https://leetcode.com/problems/minimum-cost-to-split-into-ones/

Pattern: 19 - Linear DP (Greedy/Math)

---
APPROACH: Mathematical formula
- Split n into individual 1s. Each operation splits x into a and b
  where a+b=x, costing a*b.
- Optimal: always split off 1 from the current number.
  Split x into (1, x-1) with cost 1*(x-1) = x-1.
- Total cost = (n-1) + (n-2) + ... + 1 = n*(n-1)/2.
- Proof: any split of x into a,b costs a*b. The sum of all costs
  across all splits always equals n*(n-1)/2 regardless of strategy.
  (By induction: cost(n) = a*b + cost(a) + cost(b)
   = a*b + a*(a-1)/2 + b*(b-1)/2 = (a^2 + b^2 + 2ab - a - b)/2
   = ((a+b)^2 - (a+b))/2 = n*(n-1)/2.)

Time: O(1)  Space: O(1)
---
"""


class Solution:
    def minCost(self, n: int) -> int:
        return n * (n - 1) // 2


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minCost(3) == 3    # 3->1,2 (cost 2) + 2->1,1 (cost 1) = 3
    assert sol.minCost(4) == 6    # 4->2,2 (cost 4) + 1+1 = 6. Or 4->1,3 (3)+3->1,2 (2)+2->1,1 (1)=6
    assert sol.minCost(1) == 0
    assert sol.minCost(2) == 1
    assert sol.minCost(500) == 124750

    print("all tests passed")
