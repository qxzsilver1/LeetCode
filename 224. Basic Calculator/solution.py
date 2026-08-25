class Solution:
    def calculate(self, s: str) -> int:
        def evaluate_expr():
            if not stack or type(stack[-1]) == str:
                stack.append(0)
            
            res = stack.pop()

            while stack and stack[-1] != ')':
                sign = stack.pop()

                if sign == '+':
                    res += stack.pop()
                else:
                    res -= stack.pop()
            
            return res
        
        stack = []
        n = 0
        operand = 0

        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c.isdigit():
                operand = (10 ** n * int(c)) + operand
                n += 1
            elif c != ' ':
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                
                if c == '(':
                    res = evaluate_expr()
                    stack.pop()

                    stack.append(res)
                else:
                    stack.append(c)
        
        if n:
            stack.append(operand)
        
        return evaluate_expr()
