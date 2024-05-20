class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        N = len(nums)
        mod = 10 ** 9 + 7
        res = []

        for i in range(N):
            curr = 0

            for j in range(i, N):
                curr += nums[j]
                res.append(curr)
        
        res.sort()

        return sum(res[left-1:right]) % mod
