class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(1, n+1)}

        for s, t in relations:
            adj_list[s].append(t)
        
        visited = {}

        def dfs_check_cycle(node: int) -> bool:
            if node in visited:
                return visited[node]
            else:
                visited[node] = -1
            
            for nei in adj_list[node]:
                if dfs_check_cycle(nei):
                    return True
            
            visited[node] = False

            return False
        
        for node in adj_list.keys():
            if dfs_check_cycle(node):
                return -1
        
        visited_len = {}

        def dfs_max_path(node: int) -> int:
            if node in visited_len:
                return visited_len[node]
            
            max_length = 1

            for nei in adj_list[node]:
                curr_length = dfs_max_path(nei)
                max_length = max(curr_length + 1, max_length)
            
            visited_len[node] = max_length

            return max_length
        
        return max(dfs_max_path(node) for node in adj_list.keys())
