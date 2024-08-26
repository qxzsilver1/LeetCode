class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = Counter(s)

        heap = [ (-v, k) for k, v in count_dict.items() ]
        heapq.heapify(heap)
        
        res = []

        while heap:
            v, k = heapq.heappop(heap)
            res.append(k * -v)
        
        return ''.join(res)
