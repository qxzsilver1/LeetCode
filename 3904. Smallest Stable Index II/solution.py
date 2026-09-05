class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        max_prefix = [float('-inf')] * n
        min_suffix = [float('inf')] * n
        stability_score = [0] * n

        for i in range(n):
            if i == 0:
                max_prefix[i] = nums[i]
            else:
                max_prefix[i] = max(nums[i], max_prefix[i-1])
        
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                min_suffix[i] = nums[i]
            else:
                min_suffix[i] = min(nums[i], min_suffix[i+1])
        
        smallest_stable_idx = -1

        for i in range(n):
            stability_score[i] = max_prefix[i] - min_suffix[i]

            if stability_score[i] <= k:
                smallest_stable_idx = i
                return smallest_stable_idx
        
        return smallest_stable_idx
