class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        parent = [-1] * n
        depth = [0] * n

        def find(node):
            while parent[node] != -1:
                node = parent[node]
            return node
        
        def union(node1, node2):
            node1 = find(node1)
            node2 = find(node2)

            if node1 == node2:
                return
            
            if depth[node1] < depth[node2]:
                node1, node2 = node2, node1
            
            parent[node2] = node1

            if depth[node1] == depth[node2]:
                depth[node1] += 1

        for n1, n2 in edges:
            adj_list[n1 - 1].append(n2 - 1)
            adj_list[n2 - 1].append(n1 - 1)
            union(n1 - 1, n2 - 1)
        
        num_groups_components = defaultdict(int)

        def getNumberOfGroups(src):
            q = deque()
            q.append(src)
            seen_layer = [-1] * n
            seen_layer[src] = 0
            deepest_layer = 0

            while q:
                num_nodes_in_layer = len(q)

                for _ in range(num_nodes_in_layer):
                    node = q.popleft()

                    for nei in adj_list[node]:
                        if seen_layer[nei] == -1:
                            seen_layer[nei] = deepest_layer + 1
                            q.append(nei)
                        else:
                            if seen_layer[nei] == deepest_layer:
                                return -1
                deepest_layer += 1
            
            return deepest_layer

        for node in range(n):
            num_groups = getNumberOfGroups(node)

            if num_groups == -1:
                return -1
            
            root = find(node)
            num_groups_components[root] = max(num_groups_components[root], num_groups)
        
        total_num_groups = sum(num_groups_components.values())

        return total_num_groups

        
