class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        best_val = float('inf')

        last_x = 0
        total = 0
        delta_p, delta_n = 0, 0

        for x, c in zip(nums, cost):
            total += x * c
            delta_n += c
        
        for x, c in sorted(zip(nums, cost)):
            delta = x - last_x

            total -= delta_n * delta
            total += delta_p * delta

            delta_n -= c
            delta_p += c

            best_val = min(best_val, total)
            last_x = x
        
        return best_val
