class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0]); prefixes = {}
        
        for w in words:
            for k in range(n):
                prefixes.setdefault(w[:k], []).append(w)
        
        result = []
        square = []
        
        def search():
            k = len(square)
            if k == n:
                result.append(square[:])
                return
            prefix = ''.join(w[k] for w in square)
            
            for w in prefixes.get(prefix, []):
                square.append(w)
                search()
                square.pop()
        
        search()
        
        return result
