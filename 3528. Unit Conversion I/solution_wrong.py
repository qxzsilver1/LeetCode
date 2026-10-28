class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        res = [1] * (len(conversions) + 1)

        for src, target, factor in conversions:
            res[target] = (res[src] * factor) % MOD
        
        return res
