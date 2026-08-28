class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])

        trie = {}

        for word_idx, word in enumerate(words):
            node = trie

            for char in word:
                if char in node:
                    node = node[char]
                else:
                    new_node = {}
                    new_node['#'] = []
                    node[char] = new_node
                    node = new_node
                node['#'].append(word_idx)

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
            node = trie

            for char in prefix:
                if char not in node:
                    return []
                
                node = node[char]
            
            return [words[word_idx] for word_idx in node['#']]

        for word in words:
            word_squares = [word]
            backtrack(1)
        
        return res
