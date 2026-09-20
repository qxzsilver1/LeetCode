class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0

        for i, c in enumerate(s, start= 1):
            res += (26 - (ord(c) - ord('a'))) * i
        
        return res
