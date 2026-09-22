class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def getPower(val):
            if val == 1:
                return 0
            
            power = 0

            if val % 2 == 0:
                power = getPower(val // 2) + 1
            else:
                power = getPower(3 * val + 1) + 1
            
            return power
        
        max_heap = []

        for i in range(lo, hi + 1):
            power = getPower(i)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-power, -i))
            else:
                heapq.heappushpop(max_heap, (-power, -i))
        
        power, val = heapq.heappop(max_heap)

        return -val
