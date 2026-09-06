class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        shortest_completing_word = ''
        completing_word_len = float('inf')

        plate_letters = defaultdict(int)

        for c in licensePlate:
            if c.isalpha():
                plate_letters[c.lower()] += 1
        
        for word in words:
            is_completing_word = True
            words_cnt_arr = [0] * 26

            for c in word:
                words_cnt_arr[ord(c) - ord('a')] += 1
            
            for k, v in plate_letters.items():
                words_cnt_arr[ord(k) - ord('a')] -= v

                if words_cnt_arr[ord(k) - ord('a')] < 0:
                    is_completing_word = False
                    break
                
            if is_completing_word and len(word) < completing_word_len:
                shortest_completing_word = word
                completing_word_len = len(word)
        
        return shortest_completing_word
