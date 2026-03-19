"""
2086. Minimum Number of Food Buckets to Feed the Hamsters (Medium)
https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

Given a string with 'H' (hamster) and '.' (empty), place food buckets on
'.' positions. Each hamster needs at least one adjacent food bucket.
Return minimum buckets needed, or -1 if impossible.

Pattern: Linear DP / Greedy
Approach:
- Greedy: scan left to right.
- For each hamster, prefer placing bucket to the right (covers more).
- If right is unavailable, try left.
- If neither available, return -1.
- Mark placed buckets to avoid double counting.

Time:  O(n)
Space: O(n)
"""


class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        """Return minimum food buckets needed, or -1 if impossible.

        Args:
            hamsters: String of 'H' and '.'.

        Returns:
            Minimum buckets or -1.
        """
        n = len(hamsters)
        s = list(hamsters)
        count = 0

        for i in range(n):
            if s[i] != 'H':
                continue
            # Check if already fed (bucket adjacent placed earlier)
            if i > 0 and s[i - 1] == 'B':
                continue
            # Try right first
            if i + 1 < n and s[i + 1] == '.':
                s[i + 1] = 'B'
                count += 1
            elif i > 0 and s[i - 1] == '.':
                s[i - 1] = 'B'
                count += 1
            else:
                return -1

        return count


# ---------- tests ----------
def test_minimum_buckets():
    sol = Solution()

    # Example 1: "H..H" -> place at index 1 or 2 -> 1
    assert sol.minimumBuckets("H..H") == 1

    # Example 2: ".H.H." -> 1 bucket at index 2 feeds both
    assert sol.minimumBuckets(".H.H.") == 1

    # Example 3: ".HHH." -> middle H can't be fed -> -1
    assert sol.minimumBuckets(".HHH.") == -1

    # Single hamster
    assert sol.minimumBuckets("H") == -1
    assert sol.minimumBuckets(".H") == 1
    assert sol.minimumBuckets("H.") == 1

    # No hamsters
    assert sol.minimumBuckets("...") == 0

    # Adjacent hamsters with spaces
    assert sol.minimumBuckets("H.H.H") == 2

    print("All tests passed for 2086. Minimum Number of Food Buckets to Feed the Hamsters")


if __name__ == "__main__":
    test_minimum_buckets()
