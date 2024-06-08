class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency_map = Counter(arr)

        freq_heap = list(frequency_map.values())
        heapq.heapify(freq_heap)

        res = len(freq_heap)

        while k > 0 and freq_heap:
            freq = heapq.heappop(freq_heap)

            if k >= freq:
                k -= freq
                res -= 1
        
        return res
