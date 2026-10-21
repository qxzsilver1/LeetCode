class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        max_val, min_val = max(s), min(s)

        if all(a <= b for a, b in zip(s, s[1:])):
            return 0
        
        if n == 2:
            return -1
        
        if s[0] == min_val or s[-1] == max_val:
            return 1
        
        for i in range(1, n - 1):
            if s[i] == min_val or s[i] == max_val:
                return 2
        
        return 3
