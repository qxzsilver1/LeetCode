class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0

        res = 0

        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for n in nums:
            prefix_sum += n
            remainder = prefix_sum % k

            res += prefix_cnt[remainder]
            prefix_cnt[remainder] += 1
        
        return res
