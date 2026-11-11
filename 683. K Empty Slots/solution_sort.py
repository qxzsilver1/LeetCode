class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        active = []
        
        for day, flower in enumerate(bulbs, 1):
            i = bisect.bisect(active, flower)
            
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            
            active.insert(i, flower)
        return -1
