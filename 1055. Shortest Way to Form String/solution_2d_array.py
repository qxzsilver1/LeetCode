class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_len = len(source)
        next_occurrence = [defaultdict(int) for idx in range(source_len)]

        next_occurrence[source_len - 1][source[source_len - 1]] = source_len - 1

        for idx in range(source_len - 2, -1, -1):
            next_occurrence[idx] = next_occurrence[idx + 1].copy()
            next_occurrence[idx][source[idx]] = idx
        
        source_iterator = 0
        cnt = 1

        for c in target:
            if c not in next_occurrence[0]:
                return -1
            
            if source_iterator == source_len or c not in next_occurrence[source_iterator]:
                cnt += 1
                source_iterator = 0
            
            source_iterator = next_occurrence[source_iterator][c] + 1
        
        return cnt
