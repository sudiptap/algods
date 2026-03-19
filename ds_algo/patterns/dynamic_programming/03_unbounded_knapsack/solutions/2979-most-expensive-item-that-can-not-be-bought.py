"""
2979. Most Expensive Item That Can Not Be Bought

Pattern: Unbounded Knapsack
Approach: By the Chicken McNugget theorem (Frobenius), for two coprime positive
    integers a and b, the largest number that cannot be represented as a non-negative
    combination is a*b - a - b.
Time Complexity: O(1)
Space Complexity: O(1)
"""

def mostExpensiveItem(primeOne, primeTwo):
    return primeOne * primeTwo - primeOne - primeTwo


def test():
    assert mostExpensiveItem(2, 5) == 3
    assert mostExpensiveItem(5, 7) == 23
    assert mostExpensiveItem(3, 5) == 7
    print("All tests passed!")

test()
