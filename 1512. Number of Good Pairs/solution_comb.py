class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0

        cnt_dict = Counter(nums)

        for v in cnt_dict.values():
            res += v * (v - 1) // 2
        
        return res
