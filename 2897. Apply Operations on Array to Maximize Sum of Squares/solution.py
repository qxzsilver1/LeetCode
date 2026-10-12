class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = [0] * 30 # 10^9 is possible number, and 2^30 is the possible max

        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    cnt[i] += 1
        
        res = 0

        for _ in range(k):
            curr = 0

            for j in range(29, -1, -1):
                if cnt[j] > 0:
                    curr |= 1 << j
                    cnt[j] -= 1
            
            res = (res + curr * curr) % MOD
        
        return res
