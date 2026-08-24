class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            
            if l == r:
                max_len = max(max_len, 2 * r)
            elif r > l:
                l = r = 0
        
        l = r = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            
            if l == r:
                max_len = max(max_len, 2 * l)
            elif l > r:
                l = r = 0
        
        return max_len
