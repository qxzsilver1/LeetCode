class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return float('-inf')
            
            m = (l + r) >> 1 # bit shift is same as dividing by 2

            left_sum = right_sum = curr_sum = 0

            for i in range(m-1, l-1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)
            
            curr_sum = 0

            for i in range(m + 1, r + 1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
            
            return max(dfs(l, m-1), dfs(m+1, r), left_sum + nums[m] + right_sum)
        
        return dfs(0, len(nums) - 1)
