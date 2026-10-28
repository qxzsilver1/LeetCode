class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        res = [1] * (len(conversions) + 1)

        graph = defaultdict(list)

        for src, target, factor in conversions:
            graph[src].append((target, factor))

        def dfs(source, prev):
            for target, factor in graph[source]:
                res[target] = (res[target] * prev * factor) % MOD
                dfs(target, res[target])
        
        dfs(0, 1)

        return res
