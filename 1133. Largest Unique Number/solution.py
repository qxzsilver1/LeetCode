class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)

        return max((num for num, freq in counts.items() if freq == 1), default=-1)
