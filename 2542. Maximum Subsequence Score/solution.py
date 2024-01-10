class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs_list = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs_list = sorted(pairs_list, key=lambda x: x[1], reverse=True)

        min_heap = []

        n1_sum = 0

        max_score = 0

        for n1, n2 in pairs_list:
            n1_sum += n1
            heapq.heappush(min_heap, n1)

            if len(min_heap) > k:
                n1_pop = heapq.heappop(min_heap)
                n1_sum -= n1_pop
            
            if len(min_heap) == k:
                max_score = max(max_score, n1_sum * n2)
        
        return max_score
