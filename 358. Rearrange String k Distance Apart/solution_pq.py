class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        max_heap = [(- freq, char) for char, freq in Counter(s).items()]

        heapq.heapify(max_heap)

        res = []

        while max_heap:
            tmp_items = []

            if len(max_heap) < k and - max_heap[0][0] > 1:
                return ''
            
            for _ in range(min(k, len(max_heap))):
                cnt, char = heapq.heappop(max_heap)
                res.append(char)

                if - cnt > 1:
                    tmp_items.append((cnt + 1, char))
            
            for item in tmp_items:
                heapq.heappush(max_heap, item)
        
        return ''.join(res)
