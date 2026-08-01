class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest_ptr = 0

            for i in range(l, r+1):
                farthest_ptr = max(farthest_ptr, i + nums[i])
            
            l = r + 1
            r = farthest_ptr
            res += 1
        
        return res
