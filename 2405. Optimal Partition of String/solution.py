class Solution:
    def partitionString(self, s: str) -> int:
        char_set = set()
        ctr = 1
        
        for c in s:
            if c in char_set:
                ctr += 1
                char_set = set()
            
            char_set.add(c)
        
        return ctr
            
