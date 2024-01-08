class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_open_mapping = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closing_open_mapping:
                if stack and stack[-1] == closing_open_mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
