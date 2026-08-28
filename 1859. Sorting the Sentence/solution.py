class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        n = len(s_list)

        res = [''] * (n + 1)

        for word_idx in s_list:
            res[int(word_idx[-1])] = word_idx[:-1]
        
        return ' '.join(res).strip()
