class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + (1 if num == 0 else 0))

        res = 0
        
        for l in range(len(nums)):
            low, high = l, len(nums)
            
            while low < high:
                mid = (low + high) // 2
                if prefix[mid + 1] - prefix[l] <= k:
                    low = mid + 1
                else:
                    high = mid
            res = max(res, low - l)
        return res
