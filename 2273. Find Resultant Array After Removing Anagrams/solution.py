class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res = [words[0]]
        n = len(words)

        def anagramCompare(word1, word2):
            char_freqs = [0] * 26

            for c in word1:
                char_freqs[ord(c) - ord('a')] += 1
            
            for c in word2:
                char_freqs[ord(c) - ord('a')] -= 1
            
            return all(w == 0 for w in char_freqs)
        
        for i in range(1, n):
            if anagramCompare(words[i - 1], words[i]):
                continue
            
            res.append(words[i])
        
        return res
