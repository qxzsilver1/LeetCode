class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0

        nums_squeezed = [float('-inf')] + nums + [float('-inf')]

        stack = []

        for i, n in enumerate(nums_squeezed):
            while stack and stack[-1][1] > n:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j

                res -= m * left * right
            
            stack.append((i, n))
        
        nums_squeezed = [float('inf')] + nums + [float('inf')]

        stack = []

        for i, n in enumerate(nums_squeezed):
            while stack and stack[-1][1] < n:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j

                res += m * left * right
            
            stack.append((i, n))
        
        return res
