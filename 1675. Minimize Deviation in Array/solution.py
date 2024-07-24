class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_heap = []
        max_val = 0

        for n in nums:
            tmp = n

            while not n % 2:
                n //= 2
            
            min_heap.append((n, max(2*n, tmp)))
            max_val = max(max_val, n)
        
        res = float('inf')

        heapq.heapify(min_heap)

        while len(min_heap) == len(nums):
            n, n_max = heapq.heappop(min_heap)
            res = min(res, max_val - n)

            if n < n_max:
                heapq.heappush(min_heap, (2*n, n_max))
                max_val = max(max_val, 2 * n)
        
        return res
