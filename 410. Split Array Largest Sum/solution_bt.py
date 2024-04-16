class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp = {}

        def dfs(i, m):
            if m == 1:
                return sum(nums[i:])
            
            if (i, m) in dp:
                return dp[(i, m)]
            
            res, curr_sum = float('inf'), 0

            for j in range(i, len(nums) - m + 1):
                curr_sum += nums[j]
                max_sum = max(curr_sum, dfs(j+1, m-1))

                res = min(res, max_sum)

                if curr_sum > res:
                    break
            
            dp[(i, m)] = res

            return res
        
        return dfs(0, k)
