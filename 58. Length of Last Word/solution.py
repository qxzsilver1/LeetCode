class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length_last = 0

        r = len(s) - 1
        
        while s[r] == ' ':
            r -= 1

        for i in range(r, -1, -1):
            if s[i] == ' ':
                break
            
            length_last += 1
        
        return length_last
