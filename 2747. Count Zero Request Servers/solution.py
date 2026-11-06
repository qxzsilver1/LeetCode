class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key= lambda log: log[1])

        query_ids = sorted(range(len(queries)), key= lambda i: queries[i])

        res = [0] * len(queries)
        cnt = [0] * (n + 1)

        l, r = 0, 0
        active = 0

        for i in query_ids:
            q = queries[i]

            while r < len(logs) and logs[r][1] <= q:
                server_id = logs[r][0]

                if cnt[server_id] == 0:
                    active += 1
                
                cnt[server_id] += 1
                r += 1
            
            while l < r and logs[l][1] < q - x:
                server_id = logs[l][0]
                cnt[server_id] -= 1

                if cnt[server_id] == 0:
                    active -= 1
                
                l += 1
            
            res[i] = n - active
        
        return res
                
