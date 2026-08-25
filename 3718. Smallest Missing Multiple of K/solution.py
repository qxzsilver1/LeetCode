class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen_set = set(nums)
        
        res = k

        while res in seen_set:
            res += k
        
        return res
