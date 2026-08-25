class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_heap = []
        min_heap = []
        
        j = 0
        
        res = 0

        for i, v in enumerate(nums):
            heapq.heappush(max_heap, (-v, i))
            heapq.heappush(min_heap, (v, i))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                j += 1
                
                while max_heap and max_heap[0][1] < j:
                    heapq.heappop(max_heap)
                while min_heap and min_heap[0][1] < j:
                    heapq.heappop(min_heap)

            res = max(res, i - j + 1)

        return res
