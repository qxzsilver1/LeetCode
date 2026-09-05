class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {} 
        
        def backtrack(i):
            if i == len(s):
                return ['']
            
            if i in cache:
                return cache[i]
            
            res = []

            for j in range(i, len(s)):
                w = s[i:j + 1]

                if w not in wordDict:
                    continue
                
                curr_str = backtrack(j + 1)

                if not curr_str:
                    continue
                
                for substr in curr_str:
                    sentence = w

                    if substr:
                        sentence += ' ' + substr
                    
                    res.append(sentence)
                
            cache[i] = res
            return res

        return backtrack(0)
