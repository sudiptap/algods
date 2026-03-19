"""
3259. Maximum Energy Boost From Two Drinks

Pattern: Linear DP
Approach: dp with cooldown. Two drinks A and B. If you switch, you skip one hour.
    dpA[i] = max energy at hour i drinking A. dpB[i] = max energy drinking B.
    dpA[i] = max(dpA[i-1] + A[i], dpB[i-2] + A[i])  (switch has 1 hour penalty)
    dpB[i] = max(dpB[i-1] + B[i], dpA[i-2] + B[i])
Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxEnergyBoost(energyDrinkA, energyDrinkB):
    n = len(energyDrinkA)
    if n == 1:
        return max(energyDrinkA[0], energyDrinkB[0])

    # dpA[i], dpB[i]
    ppA, ppB = energyDrinkA[0], energyDrinkB[0]  # i-2
    pA = max(ppA + energyDrinkA[1], energyDrinkB[1])  # Can't switch with only 1 hour
    pB = max(ppB + energyDrinkB[1], energyDrinkA[1])
    # Actually: at hour 0, choose A or B. At hour 1, continue or switch (but switching
    # means you skip hour 1).
    # Redefine: dpA[i] = max energy ending at hour i with drink A at hour i
    # dpA[0] = A[0], dpB[0] = B[0]
    # dpA[1] = dpA[0] + A[1]  (can't switch and get benefit at hour 1)
    # dpB[1] = dpB[0] + B[1]
    # dpA[i] = max(dpA[i-1] + A[i], dpB[i-2] + A[i])  -- switch means skip i-1
    # dpB[i] = max(dpB[i-1] + B[i], dpA[i-2] + B[i])

    ppA, ppB = energyDrinkA[0], energyDrinkB[0]
    pA, pB = ppA + energyDrinkA[1], ppB + energyDrinkB[1]

    for i in range(2, n):
        cA = max(pA + energyDrinkA[i], ppB + energyDrinkA[i])
        cB = max(pB + energyDrinkB[i], ppA + energyDrinkB[i])
        ppA, ppB = pA, pB
        pA, pB = cA, cB

    return max(pA, pB)


def test():
    assert maxEnergyBoost([1, 3, 1], [3, 1, 1]) == 5
    assert maxEnergyBoost([4, 1, 1], [1, 1, 3]) == 7
    print("All tests passed!")

test()
