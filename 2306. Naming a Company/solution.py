class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        char_map = collections.defaultdict(set)
        res = 0

        for w in ideas:
            char_map[w[0]].add(w[1:])
        
        for c1 in char_map:
            for c2 in char_map:
                if c1 == c2:
                    continue

                intersect_suffix = 0

                for w in char_map[c1]:
                    if w in char_map[c2]:
                        intersect_suffix += 1

                distinct_suffix1 = len(char_map[c1]) - intersect_suffix
                distinct_suffix2 = len(char_map[c2]) - intersect_suffix

                res += distinct_suffix1 * distinct_suffix2
    
        return res
