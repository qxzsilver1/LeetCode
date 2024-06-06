class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_to_index = {}

        res = -1

        for i, c in enumerate(s):
            if c not in char_to_index:
                char_to_index[c] = i
            else:
                res = max(res, i - char_to_index[c] - 1)
        
        return res
