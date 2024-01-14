class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = w2 = 0 # pointers for word1 and word2
        idx1 = idx2 = 0 # pointers within a word for each word within word1 and word2

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][idx1] != word2[w2][idx2]:
                return False
            
            idx1, idx2 = idx1 + 1, idx2 + 1
            if idx1 == len(word1[w1]):
                w1 += 1
                idx1 = 0
            
            if idx2 == len(word2[w2]):
                w2 += 1
                idx2 = 0
        
        return False if w1 != len(word1) or w2 != len(word2) else True
