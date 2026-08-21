class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)

        left = right = nums[0][0]

        min_heap = []

        for i in range(k):
            l = nums[i]

            left = min(left, l[0])
            right = max(right, l[0])

            heapq.heappush(min_heap, (l[0], i, 0)) # min value of that list, list idx i, and idx of ptr in that list
        
        res = [left, right]

        while True:
            num, list_i, ptr = heapq.heappop(min_heap)
            ptr += 1

            if ptr == len(nums[list_i]):
                return res

            next_val = nums[list_i][ptr]
            heapq.heappush(min_heap, (next_val, list_i, ptr))
            right = max(right, next_val)
            left = min_heap[0][0]

            if right - left < res[1] - res[0]:
                res = [left, right]
