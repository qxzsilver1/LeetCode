class Solution:
    def maxDifference(self, s: str) -> int:
        frequency = Counter(s)

        res = float('-inf')

        for odd in frequency.values():
            if odd % 2 == 0:
                continue
            
            for even in frequency.values():
                if even % 2 == 1:
                    continue
                
                res = max(res, odd - even)
        
        return res
