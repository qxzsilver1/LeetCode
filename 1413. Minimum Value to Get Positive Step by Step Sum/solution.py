class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))

        min_val = min(prefix_sum)

        return abs(min_val) + 1 if min_val < 0 else 1
