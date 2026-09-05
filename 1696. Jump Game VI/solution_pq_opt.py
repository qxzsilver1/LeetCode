class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        score = nums[0]

        pq = []
        heapq.heappush(pq, (-nums[0], 0))

        for i in range(1, n):
            while pq[0][1] < i - k:
                heapq.heappop(pq)
            
            score = nums[i] - pq[0][0]

            heapq.heappush(pq, (-score, i))
        
        return score
