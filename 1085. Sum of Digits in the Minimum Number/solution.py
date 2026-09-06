class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_elem = min(nums)

        digit_sum = 0

        while min_elem >= 10:
            digit_sum += min_elem % 10
            min_elem //= 10
        
        digit_sum += min_elem
        
        return 1 if digit_sum % 2 == 0 else 0
