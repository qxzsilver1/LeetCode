class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def update(BIT, idx, val):
            while idx > 0:
                BIT[idx] += val
                idx -= idx & (- idx)
        
        def query(BIT, idx):
            res = 0

            while (idx < len(BIT)):
                res += BIT[idx]
                idx += idx & (- idx)
            
            return res
        
        n = len(nums)
        nums_copy = [a for a in nums]

        nums_copy.sort()

        BITS = [0] * (n + 1)
        cnt = 0

        for i in range(n):
            idx = bisect_left(nums_copy, 2 * nums[i] + 1) + 1
            cnt += query(BITS, idx)
            idx = bisect_left(nums_copy, nums[i]) + 1
            update(BITS, idx, 1)
        
        return cnt
