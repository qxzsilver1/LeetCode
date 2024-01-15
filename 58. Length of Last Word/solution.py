class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length_last = 0

        r = len(s) - 1
        
        while s[r] == ' ':
            r -= 1

        while r >= 0 and s[r] != ' ':
            length_last += 1
            r -= 1
        
        return length_last
