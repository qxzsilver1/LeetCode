class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1

        heap =[(v, k) for k, v in counts.items()]
        heapq.heapify(heap)
            
        
        res = heapq.nlargest(k, heap)
        return [n for _, n in res]
