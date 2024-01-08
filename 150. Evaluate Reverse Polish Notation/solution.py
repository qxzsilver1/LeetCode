class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}

        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                if t == '/':
                    c = str(int(eval(a + '/' + b)))
                else:
                    c = eval(a + t + b)
                stack.append(str(c))
            else:
                stack.append(t)
        
        return int(stack.pop())
