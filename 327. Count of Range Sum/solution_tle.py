class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cum_sum = [0]

        for n in nums:
            cum_sum.append(cum_sum[-1] + n)
        
        cache = defaultdict(int)

        res = 0

        for val in cum_sum:
            for target in range(lower, upper + 1):
                if val - target in cache:
                    res += cache[val - target]
            
            cache[val] += 1

        return res
