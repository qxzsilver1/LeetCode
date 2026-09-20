class Solution:
    def reverseDegree(self, s: str) -> int:
        shift = ord('a')
        char_set_size = 26

        reverse_degree = 0

        for i in range(len(s)):
            reverse_degree += (char_set_size - (ord(s[i]) - shift)) * (i + 1)
        
        return reverse_degree
