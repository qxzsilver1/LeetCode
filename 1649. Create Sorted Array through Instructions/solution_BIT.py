class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def update(idx, value, bit, m):
            idx += 1

            while idx < m:
                bit[idx] += value
                idx += idx & (- idx)

        def query(idx, bit):
            idx += 1
            res = 0

            while idx >= 1:
                res += bit[idx]
                idx -= idx & (- idx)
            
            return res

        MOD = 10**9+7
        
        m = max(instructions)+2
        
        bit = [0]*m
        
        cost = 0
        
        n = len(instructions)

        for i in range(n):
            left_cost = query(instructions[i] - 1, bit)
            right_cost = i - query(instructions[i], bit)
            
            cost += min(left_cost, right_cost)
            update(instructions[i], 1, bit, m)
        
        return cost % MOD
