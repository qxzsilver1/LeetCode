class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}

        len_LIS = 0
        res = 0

        for i in range(len(nums) - 1, -1, -1):
            max_len = 1
            max_cnt = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, cnt = dp[j]

                    if length + 1 > max_len:
                        max_len = length + 1
                        max_cnt = cnt
                    elif length + 1 == max_len:
                        max_cnt += cnt
            
            if max_len > len_LIS:
                len_LIS = max_len
                res = max_cnt
            elif max_len == len_LIS:
                res += max_cnt

            dp[i] = [max_len, max_cnt]
        
        return res
