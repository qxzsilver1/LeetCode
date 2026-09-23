class Solution:
    def countLetters(self, s: str) -> int:
        res = 0
        l = 0

        for r in range(len(s) + 1):
            if r == len(s) or s[l] != s[r]:
                substr_length = r - l

                res += (1 + substr_length) * substr_length // 2
                l = r
        
        return res
