class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1) // 2

        curr_sum = sum(nums)

        if expected_sum == curr_sum:
            return 0
        else:
            return expected_sum - curr_sum
