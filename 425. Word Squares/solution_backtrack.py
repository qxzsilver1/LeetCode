class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])

        res = []
        word_squares = []

        def backtrack(step):
            nonlocal n
            if step == n:
                res.append(word_squares[:])
                return
            
            prefix = ''.join([word[step] for word in word_squares])

            for candidate in getWordsWithPrefix(prefix):
                word_squares.append(candidate)
                backtrack(step + 1)
                word_squares.pop()
        
        def getWordsWithPrefix(prefix):
            for word in words:
                if word.startswith(prefix):
                    yield word

        for word in words:
            word_squares = [word]
            backtrack(1)
        
        return res
