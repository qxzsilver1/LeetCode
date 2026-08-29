class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted(f[0] for f in flowers)
        end = sorted(f[1] for f in flowers)

        res = [0] * len(people)
        
        people_idx = sorted((p, i) for i, p in enumerate(people))

        i = j = count = 0

        for p, idx in people_idx:
            while i < len(start) and start[i] <= p:
                count += 1
                i += 1
            
            while j < len(end) and end[j] < p:
                count -= 1
                j += 1
            
            res[idx] = count

        return res
