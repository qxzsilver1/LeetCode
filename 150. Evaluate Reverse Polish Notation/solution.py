class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                b = stack.pop()
                a = stack.pop()
                t = a + b
            if t == '-':
                b = stack.pop()
                a = stack.pop()
                t = a - b
            if t == '*':
                b = stack.pop()
                a = stack.pop()
                t = a * b   
            if t == '/':
                b = stack.pop()
                a = stack.pop()
                t = int(a / b)
            stack.append(int(t))
        
        return int(stack.pop())
