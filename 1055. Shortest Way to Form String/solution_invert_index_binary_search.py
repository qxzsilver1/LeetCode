class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        char_to_indices = defaultdict(list)

        for i, c in enumerate(source):
            char_to_indices[c].append(i)
        
        source_iterator = 0
        cnt = 1

        for c in target:
            if c not in char_to_indices:
                return -1
            
            idx = bisect.bisect_left(char_to_indices[c], source_iterator)

            if idx == len(char_to_indices[c]):
                cnt += 1
                source_iterator = char_to_indices[c][0] + 1
            else:
                source_iterator = char_to_indices[c][idx] + 1
        
        return cnt
