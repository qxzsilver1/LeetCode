class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        unique_char_set = set()

        max_length = 0
        
        for end in range(len(s)):
            while s[end] in unique_char_set:
                unique_char_set.remove(s[start])
                start += 1
            
            unique_char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
        
        return max_length
