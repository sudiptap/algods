"""
1363. Largest Multiple of Three (Hard)
https://leetcode.com/problems/largest-multiple-of-three/

Problem:
    Given an array of digits, return the largest multiple of three that
    can be formed by concatenating some of the given digits in any order.
    Return "" if no such number exists.

Pattern: 19 - Linear DP

Approach:
    1. A number is divisible by 3 if its digit sum is divisible by 3.
    2. Sort digits in descending order.
    3. Compute total sum. If sum % 3 == 0, use all digits.
    4. If sum % 3 == 1, remove smallest digit with remainder 1, or two
       smallest with remainder 2.
    5. If sum % 3 == 2, remove smallest digit with remainder 2, or two
       smallest with remainder 1.
    6. Handle leading zeros: if result starts with 0, return "0".

Complexity:
    Time:  O(n log n) for sorting
    Space: O(n) for the sorted array
"""

from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        total = sum(digits)

        if total % 3 == 0:
            pass
        else:
            remainder = total % 3
            # Try removing one digit with this remainder (smallest)
            # or two digits with remainder (3 - remainder)
            def remove_one(arr, rem):
                for i in range(len(arr) - 1, -1, -1):
                    if arr[i] % 3 == rem:
                        arr.pop(i)
                        return True
                return False

            def remove_two(arr, rem):
                count = 0
                i = len(arr) - 1
                while i >= 0 and count < 2:
                    if arr[i] % 3 == rem:
                        arr.pop(i)
                        count += 1
                    i -= 1
                return count == 2

            if not remove_one(digits, remainder):
                remove_two(digits, 3 - remainder)

        if not digits:
            return ""

        result = ''.join(map(str, digits))
        if result[0] == '0':
            return "0"
        return result


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.largestMultipleOfThree([8, 1, 9]) == "981", f"Test 1 failed: {sol.largestMultipleOfThree([8, 1, 9])}"

    # Test 2
    assert sol.largestMultipleOfThree([8, 6, 7, 1, 0]) == "8760", f"Test 2 failed"

    # Test 3
    assert sol.largestMultipleOfThree([1]) == "", "Test 3 failed"

    # Test 4
    assert sol.largestMultipleOfThree([0, 0, 0, 0, 0, 0]) == "0", "Test 4 failed"

    # Test 5
    assert sol.largestMultipleOfThree([3, 3, 3]) == "333", "Test 5 failed"

    # Test 6: single zero
    assert sol.largestMultipleOfThree([0]) == "0", "Test 6 failed"

    print("All tests passed for 1363. Largest Multiple of Three!")


if __name__ == "__main__":
    run_tests()
