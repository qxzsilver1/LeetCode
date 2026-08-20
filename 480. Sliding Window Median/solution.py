class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        
        small, large = [], []

        medians = []

        for j in range(k):
            heapq.heappush(large, (nums[j], j))
        
        for _ in range(k // 2):
            num = heapq.heappop(large)
            heapq.heappush(small, (-num[0], num[1]))
        
        def get_median(small, large, k):
            return large[0][0] if k % 2 else (-small[0][0] + large[0][0]) / 2
        
        medians.append(get_median(small, large, k))

        def move(from_heap, to_heap):
            num, idx = heapq.heappop(from_heap)
            heapq.heappush(to_heap, (-num, idx))
        
        for i in range(k, len(nums)):
            if nums[i] >= large[0][0]:
                heapq.heappush(large, (nums[i], i))

                if nums[i-k] <= -small[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-nums[i], i))

                if nums[i-k] >= large[0][0]:
                    move(small, large)
            
            while large and large[0][1] < (i - k + 1):
                heapq.heappop(large)
            
            while small and small[0][1] < (i - k + 1):
                heapq.heappop(small)
            
            medians.append(get_median(small, large, k))
        
        return medians
