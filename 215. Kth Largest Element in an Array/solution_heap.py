class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            min_heap.append(-n)
        
        heapq.heapify(min_heap)

        while k > 0:
            x = - heapq.heappop(min_heap)
            k -= 1
        
        return x
