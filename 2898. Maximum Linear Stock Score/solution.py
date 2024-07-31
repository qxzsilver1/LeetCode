class Solution:
    def maxScore(self, prices: List[int]) -> int:
        sum_dict = defaultdict(int)

        for i in range(len(prices)):
            diff = prices[i] - i
            sum_dict[diff] += prices[i]
        
        return max(sum_dict.values())
