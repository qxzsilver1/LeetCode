class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0

        for n in pushed:
            stack.append(n)
            
            while i < len(popped) and stack and popped[i] == stack[-1]:
                i += 1
                stack.pop()
        
        return not stack
