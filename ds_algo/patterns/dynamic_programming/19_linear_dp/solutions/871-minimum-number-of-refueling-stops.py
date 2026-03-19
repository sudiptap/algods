"""
871. Minimum Number of Refueling Stops (Hard)
https://leetcode.com/problems/minimum-number-of-refueling-stops/

A car starts at position 0 with startFuel fuel. It needs to reach target.
Along the way there are gas stations at given positions with given fuel amounts.
Return the minimum number of refueling stops to reach target, or -1 if impossible.

Pattern: Linear DP / Greedy with Max-Heap
Approach:
- Greedy: drive as far as possible. When stuck, refuel at the passed station
  with the most fuel (max-heap).
- Iterate through stations. For each station, if we can't reach it, pop from
  the heap (best past station) until we can or the heap is empty.
- After processing all stations, check if we can reach target similarly.

Time:  O(n log n) — each station pushed/popped from heap at most once.
Space: O(n) — for the heap.
"""

import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """Return minimum refueling stops to reach target.

        Args:
            target: Distance to reach.
            startFuel: Initial fuel.
            stations: List of [position, fuel] sorted by position.

        Returns:
            Minimum stops, or -1 if impossible.
        """
        heap = []  # max-heap (store negatives)
        fuel = startFuel
        stops = 0
        prev = 0

        for pos, cap in stations:
            fuel -= (pos - prev)
            while heap and fuel < 0:
                fuel += -heapq.heappop(heap)
                stops += 1
            if fuel < 0:
                return -1
            heapq.heappush(heap, -cap)
            prev = pos

        # Try to reach target from last station
        fuel -= (target - prev)
        while heap and fuel < 0:
            fuel += -heapq.heappop(heap)
            stops += 1

        return stops if fuel >= 0 else -1


# ---------- tests ----------
def test_min_refueling_stops():
    sol = Solution()

    # Example 1: target=1, fuel=1, no stations -> 0
    assert sol.minRefuelStops(1, 1, []) == 0

    # Example 2: target=100, fuel=1, station at 10 -> impossible
    assert sol.minRefuelStops(100, 1, [[10, 100]]) == -1

    # Example 3: target=100, fuel=10, stations [[10,60],[20,30],[30,30],[60,40]]
    assert sol.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2

    # Already have enough fuel
    assert sol.minRefuelStops(50, 100, [[25, 30]]) == 0

    # Need exactly one stop
    assert sol.minRefuelStops(100, 50, [[50, 50]]) == 1

    # No stations and not enough fuel
    assert sol.minRefuelStops(100, 50, []) == -1

    print("All tests passed for 871. Minimum Number of Refueling Stops")


if __name__ == "__main__":
    test_min_refueling_stops()
