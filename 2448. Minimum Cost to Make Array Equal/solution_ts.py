class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        best_val = float('inf')

        left = 0
        right = max(nums) + 1

        def calc_dist(a):
            c = 0

            for i, x in enumerate(nums):
                c += abs(x - a) * cost[i]
            
            return c
        
        while left + 2 < right:
            mid1 = left + (right - left) // 3
            mid2 = left + (right - left) * 2 // 3

            if calc_dist(mid1) > calc_dist(mid2):
                left = mid1
            else:
                right = mid2
        
        for i in range(left, right + 1):
            best_val = min(best_val, calc_dist(i))
        
        return best_val
