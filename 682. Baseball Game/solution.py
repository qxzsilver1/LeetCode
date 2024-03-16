class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if re.match("[+-]?\d", op) is not None:
                stack.append(int(op))
                continue
            
            if op == 'C':
                stack.pop()
                continue
            
            if op == 'D':
                val = int(stack[-1]) # peek stack
                stack.append(2 * val)
                continue
            
            if op == '+':
                val2 = int(stack.pop())
                val1 = int(stack[-1]) # peek stack
                stack.append(val2)
                stack.append(val1+val2)
                continue
        
        print(stack)
        
        return sum(stack)
