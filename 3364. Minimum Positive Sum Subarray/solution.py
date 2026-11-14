class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        res = float('inf')

        for j in range(l, n + 1):
            for sub_len in range(l, min(r, j) + 1):
                curr = prefix_sum[j] - prefix_sum[j - sub_len]

                if 0 < curr < res:
                    res = curr
        
        return -1 if res == float('inf') else res
