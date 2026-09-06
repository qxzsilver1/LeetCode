class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_set = {'qwertyuiop', 'asdfghjkl', 'zxcvbnm'}
        row_map = dict()

        for i, word in enumerate(row_set):
            for c in word:
                row_map[c] = i
        
        res = []

        for word in words:
            prev_char = word[0].lower()
            same_row = True
            
            for i in range(1, len(word)):
                if row_map[word[i].lower()] != row_map[prev_char]:
                    same_row = False
                    break
                
                prev_char = word[i].lower()
            
            if same_row:
                res.append(word)
        
        return res
