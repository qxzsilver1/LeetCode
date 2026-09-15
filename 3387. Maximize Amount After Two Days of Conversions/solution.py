class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        bestConversion = defaultdict(int)
        bestConversion[initialCurrency] = 1

        def bellmanFord(pairs, rates):
            n = len(pairs)
            for _ in range(n):
                for i in range(n):
                    bestConversion[pairs[i][1]] = max(bestConversion[pairs[i][1]], bestConversion[pairs[i][0]] * rates[i])
                    bestConversion[pairs[i][0]] = max(bestConversion[pairs[i][0]], bestConversion[pairs[i][1]] / rates[i])
        
        bellmanFord(pairs1, rates1)
        bellmanFord(pairs2, rates2)

        return bestConversion[initialCurrency]
