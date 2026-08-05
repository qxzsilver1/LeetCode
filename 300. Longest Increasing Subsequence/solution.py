class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_incr_subseq = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    longest_incr_subseq[i] = max(longest_incr_subseq[i], 1 + longest_incr_subseq[j])
        
        return max(longest_incr_subseq)
