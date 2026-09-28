class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        streak = 0
        res = 0

        for c in s:
            if c == '1':
                streak += 1
                res = (res + streak) % MOD
            else:
                streak = 0
        
        return res
