class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        flip_ctr = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                flip_ctr += 1
            
        return not flip_ctr > 1
