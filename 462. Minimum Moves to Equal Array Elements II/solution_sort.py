class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        min_val = float('inf')
        n = len(nums)

        nums.sort()

        curr_sum = total = 0

        for num in nums:
            total += num
        
        for i in range(n):
            val = (nums[i] * i - curr_sum) + ((total - curr_sum) - nums[i] * (n - i))

            min_val = min(min_val, val)

            curr_sum += nums[i]
        
        return min_val
