"""
3218. Minimum Cost for Cutting Cake I

Pattern: Linear DP (Greedy)
Approach: Greedy sort cuts by cost descending. When making a horizontal cut, it
    applies to all current vertical pieces, and vice versa. Process cuts in
    decreasing cost order. Each h-cut costs h * v_pieces, each v-cut costs v * h_pieces.
Time Complexity: O(m*log(m) + n*log(n))
Space Complexity: O(1)
"""

def minimumCost(m, n, horizontalCut, verticalCut):
    horizontalCut.sort(reverse=True)
    verticalCut.sort(reverse=True)
    h_pieces = 1  # number of horizontal pieces
    v_pieces = 1
    i = j = 0
    cost = 0

    while i < len(horizontalCut) and j < len(verticalCut):
        if horizontalCut[i] >= verticalCut[j]:
            cost += horizontalCut[i] * v_pieces
            h_pieces += 1
            i += 1
        else:
            cost += verticalCut[j] * h_pieces
            v_pieces += 1
            j += 1

    while i < len(horizontalCut):
        cost += horizontalCut[i] * v_pieces
        i += 1
    while j < len(verticalCut):
        cost += verticalCut[j] * h_pieces
        j += 1

    return cost


def test():
    assert minimumCost(3, 2, [1, 3], [5]) == 13
    assert minimumCost(2, 2, [7], [4]) == 15
    print("All tests passed!")

test()
