class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9+7
        current = []
        cost = 0
        
        for x in instructions:
            left_cost = bisect.bisect_left(current, x)
            right_cost = len(current) - bisect.bisect_right(current, x)
            cost += min(left_cost, right_cost)
            bisect.insort(current, x)
            cost %= MOD
        
        return cost % MOD
