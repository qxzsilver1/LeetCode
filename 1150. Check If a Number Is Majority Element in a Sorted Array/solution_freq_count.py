class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        count = 0
        for num in nums:
            count = count + 1 if num == target else count

        return count > len(nums) // 2
