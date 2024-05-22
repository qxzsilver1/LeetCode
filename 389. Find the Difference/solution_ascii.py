class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_sum = 0

        for c in t:
            char_sum += ord(c)
        
        for c in s:
            char_sum -= ord(c)
        
        return chr(char_sum)
