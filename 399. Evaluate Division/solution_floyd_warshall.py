class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    if j not in graph[i]:
                        graph[i][j] = graph[i][k] * graph[k][j]

        result = []
        
        for a, b in queries:
            if a in graph and b in graph[a]:
                result.append(graph[a][b])
            else:
                result.append(-1.0)
        return result
