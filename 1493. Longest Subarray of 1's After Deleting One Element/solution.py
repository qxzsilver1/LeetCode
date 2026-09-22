class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zero_cnt = 0

        longest_window = 0

        l = 0

        for i in range(len(nums)):
            zero_cnt += (1 if nums[i] == 0 else 0)

            while zero_cnt > 1:
                zero_cnt -= (1 if nums[l] == 0 else 0)
                l += 1
            
            longest_window = max(longest_window, i - l)
        
        return longest_window
