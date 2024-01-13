class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        
        n = len(nums)

        l, r = 0, k
        max_avg = nums[0]
        
        for i in range(0, r):
            max_avg = (i * max_avg + nums[i]) / (i+1)
        
        curr_avg = max_avg

        while r < n:
            curr_avg -= nums[l] / k
            curr_avg += nums[r] / k

            max_avg = max(max_avg, curr_avg)

            l += 1
            r += 1
        
        return max_avg
