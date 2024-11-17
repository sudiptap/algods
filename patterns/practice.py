# find upper and lower bound
import heapq

data = [10, 2, 20, 4, -80, 70]

class MaxHeapNode:
    def __init__(self, data):
        self.data = data
    
    def __gt__(self, other):
        return self.data < other.data

    # def __repr__(self):
    #     return self.data
    
    # def __str__(self):
    #     return self.data

h = []
for d in data:
    heapq.heappush(h, MaxHeapNode(d))

while h:
    ele = heapq.heappop(h)
    print(ele.data)