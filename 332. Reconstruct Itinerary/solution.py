class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        for src, dst in sorted(tickets)[::-1]:
            adj_list[src].append(dst)
        
        res = []

        def dfs(s):
            while adj_list[s]:
                t = adj_list[s].pop()
                dfs(t)
            
            res.append(s)
        
        dfs('JFK')

        return res[::-1]
