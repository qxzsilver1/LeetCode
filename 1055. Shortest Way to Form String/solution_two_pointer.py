class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_chars = set(source)

        for c in target:
            if c not in source_chars:
                return -1
        
        m = len(source)
        source_iterator = 0

        cnt = 0

        for c in target:
            if source_iterator == 0:
                cnt += 1
            
            while source[source_iterator] != c:
                source_iterator = (source_iterator + 1) % m

                if source_iterator == 0:
                    cnt += 1
            
            source_iterator = (source_iterator + 1) % m
        
        return cnt
