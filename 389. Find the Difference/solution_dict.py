class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        original_chars_dict = Counter(s)

        for c in t:
            if c not in original_chars_dict:
                return c
            
            original_chars_dict[c] -= 1

            if original_chars_dict[c] < 0:
                return c
