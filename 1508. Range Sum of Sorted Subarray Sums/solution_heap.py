class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        N = len(nums)
        mod = 10 ** 9 + 7
        
        min_heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(min_heap)

        res = 0

        for i in range(right):
            num, idx = heapq.heappop(min_heap)
            if i >= left - 1:
                res = (res + num) % mod
            
            if idx + 1 < n:
                next_pair = (num + nums[idx+1], idx + 1)
                heapq.heappush(min_heap, next_pair)
        
        return res

        
