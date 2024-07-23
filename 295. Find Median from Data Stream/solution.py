class MedianFinder:

    def __init__(self):
        self.lower, self.higher = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -1 * num)

        if self.lower and self.higher and (-1 * self.lower[0] > self.higher[0]):
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.higher, val)
        
        if len(self.lower) > len(self.higher) + 1:
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.higher, val)
        
        if len(self.lower) + 1 < len(self.higher):
            val = heapq.heappop(self.higher)
            heapq.heappush(self.lower, -1 * val)
    

    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return -self.lower[0]
        
        if len(self.lower) < len(self.higher):
            return self.higher[0]
        
        return (-self.lower[0] + self.higher[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
