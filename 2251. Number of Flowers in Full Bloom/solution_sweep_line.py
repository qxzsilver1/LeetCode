class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        
        for start, end in flowers:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort()
        
        queries = sorted((p, i) for i, p in enumerate(people))
        
        res = [0] * len(people)

        count = j = 0

        for time, idx in queries:
            while j < len(events) and events[j][0] <= time:
                count += events[j][1]
                j += 1
            
            res[idx] = count

        return res
