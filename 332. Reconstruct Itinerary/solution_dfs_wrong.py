class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = { src: [] for src, _ in tickets}

        tickets.sort()

        for src, dst in tickets:
            adj_list[src].append(dst)
        
        res = ['JFK']

        def dfs(s):
            if len(res) == len(tickets) + 1:
                return True
            
            if s not in adj_list:
                return False
            
            tmp = list(adj_list[s])
            for i, v in enumerate(tmp):
                adj_list[s].pop(i)
                res.append(v)

                if dfs(v):
                    return True
                
                adj_list[s].insert(i, v)
                res.pop()
            
            return False
        
        dfs('JFK')

        return res
