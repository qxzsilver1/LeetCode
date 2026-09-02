class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count_similar = defaultdict(int)

        for word in words:
            val = ''.join(sorted(set(word)))
            count_similar[val] += 1
        
        res = 0

        for key, val in count_similar.items():
            res += math.comb(val, 2) if val >= 2 else 0
        
        return res
