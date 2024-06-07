class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()

        res = ' '.join(words)
        return res
