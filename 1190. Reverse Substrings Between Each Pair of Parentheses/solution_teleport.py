class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs = {}
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pairs[i] = j
                pairs[j] = i
        
        i = 0
        direction = 1

        res = []

        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = pairs[i]
                direction *= -1
            else:
                res.append(s[i])
            
            i += direction

        return ''.join(res)
