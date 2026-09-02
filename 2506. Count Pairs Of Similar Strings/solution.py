class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count_similar = defaultdict(int)

        alphabet_map = [0] * 26

        for word in words:
            for c in word:
                if alphabet_map[ord(c) - ord('a')] == 1:
                    continue
                else:
                    alphabet_map[ord(c) - ord('a')] = 1
            val = ''.join([str(a) for a in alphabet_map])
            count_similar[val] += 1

            alphabet_map = [0] * 26
        
        res = 0

        for key, val in count_similar.items():
            res += math.comb(val, 2) if val >= 2 else 0
        
        return res
