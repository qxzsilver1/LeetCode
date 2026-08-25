class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 1

        for i in range(1, 2*n):
            if nums[i % n] >= nums[(i - 1) % n]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt == n:
                return True
            
        return n == 1
