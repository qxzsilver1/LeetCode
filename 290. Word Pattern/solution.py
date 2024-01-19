class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(words) != len(pattern):
            return False
        
        pattern_to_str = {}
        str_to_pattern = {}

        for i in range(len(pattern)):
            if pattern[i] not in pattern_to_str and words[i] not in str_to_pattern:
                pattern_to_str[pattern[i]] = words[i]
                str_to_pattern[words[i]] = pattern[i]
            
            if pattern_to_str[pattern[i]] != words[i] or str_to_pattern[words[i]] != pattern[i]:
                return False
        
        return True
