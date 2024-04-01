class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        
        res = ''

        while stack:
            char, count = stack[-1]
            res += char * count
            stack.pop()
        
        return res[::-1]
            
