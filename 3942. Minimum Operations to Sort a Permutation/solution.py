class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        start = nums.index(0)

        asc, desc = True, True

        for i in range(1, n):
            val = nums[(start + i) % n]

            if val != i:
                asc = False
            
            if val != n - i:
                desc = False
            
            if not asc and not desc:
                return -1
        
        return min(start, n - start + 2) if asc else min(n - start, start + 2)
