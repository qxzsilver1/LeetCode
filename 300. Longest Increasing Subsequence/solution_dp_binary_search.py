from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        longest_incr_subseq = 1

        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                longest_incr_subseq += 1
                continue
            
            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]
        
        return longest_incr_subseq
