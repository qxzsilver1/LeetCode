class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        res = ''

        for c in s:
            if c != '*':
                stack.append(c)
            elif s and c == '*':
                stack.pop()
        
        while stack:
            res += stack.pop()
        
        return res[::-1]
