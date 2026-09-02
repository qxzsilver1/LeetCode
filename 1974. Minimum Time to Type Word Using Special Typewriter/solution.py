class Solution:
    def minTimeToType(self, word: str) -> int:
        n = len(word)

        prev_char = ord('a')

        res = n

        for c in word:
            res += min((ord(c) - prev_char) % 26, (prev_char - ord(c)) % 26)
            prev_char = ord(c)
        
        return res
