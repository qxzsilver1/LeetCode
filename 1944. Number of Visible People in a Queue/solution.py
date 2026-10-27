class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        res = [0] * n

        stack = []

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] < h:
                res[stack.pop()] += 1
            
            if stack:
                res[stack[-1]] += 1
            
            stack.append(i)
        
        return res
