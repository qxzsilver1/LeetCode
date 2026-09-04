class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(set)
        indegrees = [0] * n

        res = []

        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
            indegrees[u] += 1
            indegrees[v] += 1
        
        indegree_map = Counter(indegrees)

        indegree_map = {k: v for k, v in sorted(indegree_map.items(), key=lambda item: item[0])}

        indegree_node_map = defaultdict(list)

        for i, v in enumerate(indegrees):
            indegree_node_map[v].append(i)

        print(indegree_map)
        print(indegree_node_map)

        visited_set = set()
        q = deque()

        if 1 in indegree_node_map:
            curr_row = []
            node = indegree_node_map[1][0]

            q.append(node)

            while q:
                node = q.popleft()
                visited_set.add(node)
                curr_row.append(node)

                for nei in adj_list[node]:
                    if nei not in visited_set:
                        node = nei
                        q.append(node)
                        break
                    else:
                        continue
            
            res.append(curr_row)
        elif 2 in indegree_node_map and 4 not in indegree_node_map:
            curr_row = []
            node = indegree_node_map[2][0]

            curr_row.append(node)
            visited_set.add(node)

            for nei in adj_list[node]:
                if indegrees[nei] == 2:
                    curr_row.append(nei)
                    visited_set.add(nei)
                    break
                else:
                    continue
            res.append(curr_row)
            n_col = len(curr_row)

            for i in range(1, n // n_col):
                curr_row = []

                for j in range(n_col):
                    for nei in adj_list[res[i-1][j]]:
                        if nei not in visited_set and res[i-1][j] in adj_list[nei]:
                            visited_set.add(nei)
                            curr_row.append(nei)
                        else:
                            continue
                
                res.append(curr_row)
        else:
            curr_row = []
            node = indegree_node_map[2][0]

            q.append(node)

            while q:
                node = q.popleft()
                visited_set.add(node)
                curr_row.append(node)

                for nei in adj_list[node]:
                    if nei not in visited_set and indegrees[nei] == 3:
                        node = nei
                        q.append(node)
                        break
                    elif nei not in visited_set and indegrees[nei] == 2:
                        node = nei
                        visited_set.add(node)
                        curr_row.append(node)
                        break
                    else:
                        continue
            
            res.append(curr_row)

            n_col = len(curr_row)

            for i in range(1, n // n_col):
                curr_row = []

                for j in range(n_col):
                    for nei in adj_list[res[i-1][j]]:
                        if nei not in visited_set and res[i-1][j] in adj_list[nei]:
                            visited_set.add(nei)
                            curr_row.append(nei)
                        else:
                            continue
                
                res.append(curr_row)




        # for i in range(1, 5):
        #     if i not in indegree_node_map:
        #         continue
            
        #     q = deque()
        #     row = []
            
        #     for node in indegree_node_map[i]:
        #         if visited[node]:
        #             continue
                
        #         row.append(node)
        #         q.append(node)
        #         visited[node] = True

        #         j = 0

        #         for nei in adj_list[node]:
        #             while indegrees[nei] = i + 1:
        #                 if len(res) == 0:
        #                     row.append(nei)
        #                     q.append(nei)
        #                     visited[nei] = True
                            
        #                     for new_nei in adj_list[nei]:
        #                         if indegrees[new_nei] == i + 1:
        #                             new_nei = nei
        #                             break
        #                 else:
        #                     prev_idx = len(res) - 1

        #                     if nei not in visited and indegrees[nei] == i + 1:
        #                         if adj_list[nei] 


                
        return res
        
