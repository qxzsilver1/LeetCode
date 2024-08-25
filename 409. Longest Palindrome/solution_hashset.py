class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen_chars = set()
        res = 0

        for c in s:
            if c in seen_chars:
                seen_chars.remove(c)
                res += 2
            else:
                seen_chars.add(c)
        
        return res + 1 if seen_chars else res
