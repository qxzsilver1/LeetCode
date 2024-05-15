class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def calc_cost(target):
            res = 0
            
            for x, c in zip(nums, cost):
                res += abs(x - target) * c
            
            return res
        
        l, r = min(nums), max(nums)

        while (l <= r):
            target = l + (r - l) // 2

            curr_cost = calc_cost(target)
            left_cost = calc_cost(target - 1)
            right_cost = calc_cost(target + 1)

            if right_cost >= curr_cost <= left_cost:
                return curr_cost
            elif left_cost < curr_cost:
                r = target - 1
            else:
                l = target + 1
        
        return l
