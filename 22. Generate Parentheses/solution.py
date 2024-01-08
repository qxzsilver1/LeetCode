class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []

        def backtracker(open_num, close_num):
            if open_num == close_num == n:
                output.append(''.join(stack))
                return
            
            if open_num < n:
                stack.append('(')
                backtracker(open_num + 1, close_num)
                stack.pop()
            
            if close_num < open_num:
                stack.append(')')
                backtracker(open_num, close_num + 1)
                stack.pop()
        backtracker(0, 0)
        
        return output
            
