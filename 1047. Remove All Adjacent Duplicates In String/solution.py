class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        res = ''

        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        
        while stack:
            res += stack.pop()
        
        return res[::-1]
        # return ''.join(stack)
            
