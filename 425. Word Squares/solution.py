class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        prefix_hashmap = {}

        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                prefix_hashmap.setdefault(prefix, set()).add(word)

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
            if prefix in prefix_hashmap:
                return prefix_hashmap[prefix]
            else:
                return set([])

        for word in words:
            word_squares = [word]
            backtrack(1)
        
        return res
