class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_dict = {0: -1}

        curr_sum = 0
        max_len = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            diff = curr_sum - k

            if diff in sum_dict:
                max_len = max(max_len, i - sum_dict[diff])
            
            if curr_sum not in sum_dict:
                sum_dict[curr_sum] = i
        
        return max_len
