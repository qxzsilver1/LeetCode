class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        min_heap = []

        for r in range(min(k, n)):
            min_heap.append((matrix[r][0], r, 0))
        
        heapq.heapify(min_heap)
        
        while k:
            element, r, c = heapq.heappop(min_heap)

            if c < n-1:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))

            k -= 1
        
        return element
