class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[[0, 0], [nums[0], 1]]]

        def bs1(num):
            l, r = 0, len(dp) - 1
            j = len(dp) - 1
            while l <= r:
                mid = (l + r) // 2
                if dp[mid][-1][0] < num:
                    l = mid + 1
                else:
                    j = mid
                    r = mid - 1
            return j

        def bs2(i, num):
            if i < 0:
                return 1
            l, r = 1, len(dp[i]) - 1
            j = 0
            while l <= r:
                mid = (l + r) // 2
                if dp[i][mid][0] >= num:
                    j = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return dp[i][-1][1] - dp[i][j][1]

        LIS = 1
        
        for i in range(1, n):
            num = nums[i]
            if num > dp[-1][-1][0]:
                count = bs2(LIS - 1, num)
                dp.append([[0, 0], [num, count]])
                LIS += 1
            else:
                j = bs1(num)
                count = bs2(j - 1, num)
                dp[j].append([num, dp[j][-1][1] + count])

        return dp[-1][-1][1]
