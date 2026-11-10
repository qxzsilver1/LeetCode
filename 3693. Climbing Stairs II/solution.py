class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a = b = c = 0

        for i in range(n):
            # alternatively, the lines below can all be written in one liner as:
            # a, b, c = b, c, min(a + 9, b + 4, c + 1) + costs[i]
            tmp1 = b
            tmp2 = c
            tmp3 = min(a + 9, b + 4, c + 1) + costs[i]

            a = tmp1
            b = tmp2
            c = tmp3
        
        return c
