class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = [p for p in prices]

        monotonic_stack = []

        for i in range(len(prices)):
            while monotonic_stack and prices[monotonic_stack[-1]] >= prices[i]:
                j = monotonic_stack.pop()
                res[j] -= prices[i] 
            monotonic_stack.append(i)

        return res
