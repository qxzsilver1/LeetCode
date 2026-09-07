class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        stack = []

        max_val = float('-inf')

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            
            if num > max_val:
                stack.append(num)
            
            max_val = max(max_val, num)
        
        return len(stack)
