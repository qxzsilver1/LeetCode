class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0
        
        graph = {}

        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
        
        curr_layer = set([0])
        last_layer = set([n-1])

        visited = {0, n - 1}
        step = 0

        while curr_layer:
            if len(curr_layer) > len(last_layer):
                curr_layer, last_layer = last_layer, curr_layer
            
            next_layer = set()

            for node in curr_layer:
                for child in graph[arr[node]]:
                    if child in last_layer:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        next_layer.add(child)
                
                graph[arr[node]].clear()

                for child in [node - 1, node + 1]:
                    if child in last_layer:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        next_layer.add(child)
            curr_layer = next_layer
            step += 1
        
        return -1
