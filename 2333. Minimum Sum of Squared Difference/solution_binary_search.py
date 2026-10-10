class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2

        n = len(nums1)

        max_diff = 0

        for i in range(n):
            nums1[i] = abs(nums1[i] - nums2[i])
            max_diff = max(max_diff, nums1[i])
        
        l, r = 0, max_diff
        res = 0

        while l <= r:
            m = (l + r) >> 1

            if sum(num - m for num in nums1 if num > m) <= k:
                r = m - 1
                res = m
            else:
                l = m + 1
        
        for num in nums1:
            if num > res:
                k -= num - res
        
        nums1.sort(reverse= True)

        ans = 0

        for num in nums1:
            diff = min(num, res)
            
            if k > 0 and diff > 0:
                diff -= 1
                k -= 1
            ans += diff ** 2
        
        return ans
