class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_count1 = Counter(s1.split())
        s1_keyset = set(word_count1.keys())
        word_count2 = Counter(s2.split())
        s2_keyset = set(word_count2.keys())

        diff_keyset = s1_keyset ^ s2_keyset

        res = []

        for k in diff_keyset:
            if k in word_count1 and word_count1[k] == 1 or k in word_count2 and word_count2[k] == 1:
                res.append(k)
            else:
                continue
        
        return res
        
