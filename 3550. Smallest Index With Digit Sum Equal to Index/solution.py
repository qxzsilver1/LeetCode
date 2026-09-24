class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digit_sum = 0

            while num:
                num, digit = divmod(num, 10)
                digit_sum += digit
            
            if digit_sum == i:
                return i
        
        return -1
