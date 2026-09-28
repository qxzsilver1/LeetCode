class Solution:
    def addMinimum(self, word: str) -> int:
        k = 0
        prev_char = 'z'

        for c in word:
            if c <= prev_char:
                k += 1
            prev_char = c
        
        return 3*k - len(word)
