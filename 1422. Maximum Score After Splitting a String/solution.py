class Solution:
    def maxScore(self, s: str) -> int:
        num_zeroes = 0
        num_ones = s.count('1')

        res = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                num_zeroes += 1
            else:
                num_ones -= 1
            
            res = max(res, num_zeroes + num_ones)
        
        return res
