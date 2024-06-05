class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []

        cnt = Counter(words[0])
        
        for w in words[1:]:
            curr_cnt = Counter(w)

            for c in cnt:
                cnt[c] = min(cnt[c], curr_cnt[c])
        
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)
        
        return res
