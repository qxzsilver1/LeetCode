class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt_less, cnt_equal = 0, 0

        for num in nums:
            if num < target:
                cnt_less += 1
            elif num == target:
                cnt_equal += 1
        
        res = list(range(cnt_less, cnt_less + cnt_equal))

        return res
