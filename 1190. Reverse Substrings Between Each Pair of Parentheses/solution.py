class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                string_portion = []

                while stack[-1] != '(':
                    string_portion.append(stack.pop())
                stack.pop()
                stack.extend(string_portion)
            else:
                stack.append(c)
        
        return ''.join(stack)
