class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)

        min_num, max_num = min(nums), max(nums)

        return [x for x in range(min_num+1, max_num) if x not in num_set]
