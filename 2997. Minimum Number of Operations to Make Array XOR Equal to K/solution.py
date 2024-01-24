class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_ones = defaultdict(int)

        for n in nums:
            for i in range(32):
                num_ones[i] += (n >> i) & 1
        
        res = 0

        for i in range(32):
            kth_bit = (k >> i) & 1

            if kth_bit and num_ones[i] % 2 == 0:
                    res += 1
            elif not kth_bit and num_ones[i] % 2 == 1:
                res += 1

        return res 
