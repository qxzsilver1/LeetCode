class Solution:
    def treeDiameter(self, edges: list[list[int]]) -> int:
        graph = [set() for i in range(len(edges)+1)]
        
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = []
        
        for vertex, links in enumerate(graph):
            if len(links) == 1:
                leaves.append(vertex)
        
        layers = 0
        vertex_left = len(edges) + 1
        
        while vertex_left > 2:
            vertex_left -= len(leaves)
            next_leaves = []
            
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    next_leaves.append(neighbor)
            
            layers += 1
            leaves = next_leaves
        
        return layers * 2 + (0 if vertex_left == 1 else 1)
