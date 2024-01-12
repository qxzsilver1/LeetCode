class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        output = r

        while l <= r:
            k = l + (r - l) // 2

            hours = 0

            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                output = min(output, k)
                r = k - 1
            else:
                l = k + 1
        
        return output
