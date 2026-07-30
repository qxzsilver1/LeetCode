class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(1, n+1)}

        for s, t in relations:
            adj_list[s].append(t)
        
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            else:
                visited[node] = -1
            
            max_length = 1

            for nei in adj_list[node]:
                curr_len = dfs(nei)

                if curr_len == -1:
                    return -1
                else:
                    max_length = max(curr_len + 1, max_length)
            
            visited[node] = max_length
            
            return max_length

        max_length = -1

        for node in adj_list.keys():
            curr_len = dfs(node)

            if curr_len == -1:
                return -1
            else:
                max_length = max(curr_len, max_length)

        return max_length
