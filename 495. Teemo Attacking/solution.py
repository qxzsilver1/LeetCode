class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)

        if n == 0:
            return 0
        
        res = 0

        for i in range(n - 1):
            res += min(timeSeries[i + 1] - timeSeries[i], duration)
        
        return res + duration
