class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''

                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                k = ''

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(substr * int(k))
        
        while stack:
            res = stack.pop() + res
        
        return res
        # return ''.join(stack) # use this instead the while stack loop and res append
