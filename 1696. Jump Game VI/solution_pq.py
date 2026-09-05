class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        scores = [0] * n

        scores[0] = nums[0]

        pq = []
        heapq.heappush(pq, (-nums[0], 0))

        for i in range(1, n):
            while pq[0][1] < i - k:
                heapq.heappop(pq)
            
            scores[i] = scores[pq[0][1]] + nums[i]

            heapq.heappush(pq, (-scores[i], i))
        
        return scores[-1]
