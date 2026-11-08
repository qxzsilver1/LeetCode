class Solution:
    def queryConversions(self, conversions: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        n = len(conversions) + 1

        graph = [[] for _ in range(n)]

        for a, b, factor in conversions:
            graph[a].append((b, factor))
            graph[b].append((a, pow(factor, MOD - 2, MOD)))
        
        weight = [0] * n
        weight[0] = 1

        stack = [0]

        while stack:
            u = stack.pop()

            for v, factor in graph[u]:
                if weight[v] == 0:
                    weight[v] = weight[u] * factor % MOD
                    stack.append(v)
        
        return [weight[b] * pow(weight[a], MOD - 2, MOD) % MOD for a, b in queries]
