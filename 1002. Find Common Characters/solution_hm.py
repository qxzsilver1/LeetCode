class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_boolean = [0] * 26
        offset = ord('a')
        res = []

        for j in range(len(words)):
            curr_word_dict = Counter(words[j])

            for i in range(len(char_boolean)):
                if chr(offset + i) not in curr_word_dict:
                    char_boolean[i] = 0
                else:
                    char_boolean[i] = curr_word_dict[chr(offset + i)] if j == 0 else min(curr_word_dict[chr(offset + i)], char_boolean[i])
        
        for i in range(len(char_boolean)):
            if char_boolean[i]:
                for j in range(char_boolean[i]):
                    res.append(chr(offset + i))
        
        return res

