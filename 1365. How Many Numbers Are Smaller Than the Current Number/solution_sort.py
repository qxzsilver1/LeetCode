class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        nums_sorted = list(enumerate(nums))
        nums_sorted.sort(key= lambda x: x[1])

        num_to_new_idx_map = {}

        for i, v in enumerate(nums_sorted):
            if v[1] not in num_to_new_idx_map:
                num_to_new_idx_map[v[1]] = i
        
        res = []

        for num in nums:
            res.append(num_to_new_idx_map[num])
        
        return res
