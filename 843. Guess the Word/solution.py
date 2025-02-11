# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        
        def distance(w1, w2):
            matches = 0

            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    matches += 1
            return matches
        
        word_match_map = { word: {} for word in words }

        for w1 in words:
            for w2 in words:
                dist = distance(w1, w2)
                word_match_map[w1][w2] = dist

        candidate_words = words[:]

        while candidate_words:
            bucketSizeMap = {}

            for guess_word in candidate_words:
                matchBucketMap = {}

                for word in candidate_words:
                    dist = word_match_map[guess_word][word]

                    if dist not in matchBucketMap:
                        matchBucketMap[dist] = 0
                    
                    matchBucketMap[dist] += 1
                
                bucketSizeMap[guess_word] = max(matchBucketMap.values())
            
            final_guess_word = min(bucketSizeMap, key=bucketSizeMap.get)

            guess_value = master.guess(final_guess_word)

            if guess_value == 6:
                return

            candidate_words = [ w for w in candidate_words if word_match_map[final_guess_word][w] == guess_value]
