# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def distance(self, word1: str, word2: str) -> int:
        if len(word1) != len(word2):
            return -2
        
        matches = 0
        
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                matches += 1

        return matches
    
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        for i, match in zip(range(0, 10), range(0, 6)):
            word_cnt = defaultdict(int)

            for w1 in words:
                for w2 in words:
                    if self.distance(w1, w2) == 0:
                        word_cnt[w1] += 1

            min_max = (words[0], 10000)

            for w in words:
                if w in word_cnt and word_cnt[w] <= min_max[1]:
                    min_max = (w, word_cnt[w])
            
            master_match = master.guess(min_max[0])
            candidate_words = []

            for w in words:
                if self.distance(w, min_max[0]) == master_match:
                    candidate_words.append(w)
            
            words = candidate_words
