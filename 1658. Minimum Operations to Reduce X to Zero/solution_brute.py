class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        res = n + 1
        suffixSum = prefixSum = 0

        for i in range(n - 1, -1, -1):
            suffixSum += nums[i]
            if suffixSum == x:
                res = min(res, n - i)

        for i in range(n):
            prefixSum += nums[i]
            suffixSum = 0
            if prefixSum == x:
                res = min(res, i + 1)

            for j in range(n - 1, i, -1):
                suffixSum += nums[j]
                if prefixSum + suffixSum == x:
                    res = min(res, i + 1 + n - j)

        return -1 if res == n + 1 else res
