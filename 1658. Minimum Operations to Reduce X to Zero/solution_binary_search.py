class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        if x > prefixSum[n]:
            return -1

        def binarySearch(target, m):
            l, r = 1, m
            index = n + 1

            while l <= r:
                mid = (l + r) >> 1
                if prefixSum[mid] >= target:
                    if prefixSum[mid] == target:
                        index = mid
                    r = mid - 1
                else:
                    l = mid + 1

            return index

        res = binarySearch(x, n)
        suffixSum = 0
        
        for i in range(n - 1, 0, -1):
            suffixSum += nums[i]
            if suffixSum == x:
                res = min(res, n - i)
                break
            if suffixSum > x: break
            res = min(res, binarySearch(x - suffixSum, i) + n - i)

        return -1 if res == n + 1 else res
