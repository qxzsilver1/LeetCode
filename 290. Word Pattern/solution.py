class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(words) != len(pattern):
            return False
        
        pattern_to_str = [''] * 26
        str_to_pattern = {}

        for i in range(len(pattern)):
            ord_val = ord(pattern[i]) - ord('a')
            
            if not pattern_to_str[ord_val] and words[i] not in str_to_pattern:
                pattern_to_str[ord_val] = words[i]
                str_to_pattern[words[i]] = chr(ord_val + ord('a'))
            
            if pattern_to_str[ord_val] != words[i] or str_to_pattern[words[i]] != pattern[i]:
                return False
        
        return True
