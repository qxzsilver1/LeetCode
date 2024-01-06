class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        start = end = 0
        max_length = 0
        
        unique_char_set = set()
        
        while end < len(s):
            if s[end] not in unique_char_set:
                unique_char_set.add(s[end])
                end += 1
                max_length = max(max_length, len(unique_char_set))
            else:
                unique_char_set.remove(s[start])
                start += 1
        
        return max_length
