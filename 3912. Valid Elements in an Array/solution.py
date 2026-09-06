class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        max_prefix_arr, max_suffix_arr = [0] * n, [0] * n

        for i in range(n):
            if i == 0:
                max_prefix_arr[i] = nums[i]
                continue
            max_prefix_arr[i] = max(nums[i], max_prefix_arr[i - 1])
        
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                max_suffix_arr[i] = nums[i]
                continue
            max_suffix_arr[i] = max(nums[i], max_suffix_arr[i + 1])
        
        res = []

        for i in range(n):
            if i == 0 or i == n - 1 or nums[i] > max_prefix_arr[i-1] or nums[i] > max_suffix_arr[i+1]:
                res.append(nums[i])
        
        return res
