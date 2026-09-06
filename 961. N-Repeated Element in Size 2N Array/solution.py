class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for k in counts:
            if counts[k] > 1:
                return k
