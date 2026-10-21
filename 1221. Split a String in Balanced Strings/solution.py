class Solution:
    def balancedStringSplit(self, s: str) -> int:
        curr_val = 0
        splits = 0

        for c in s:
            if c == 'R':
                curr_val += 1
            else:
                curr_val += -1
            
            if curr_val == 0:
                splits += 1
        
        return splits
