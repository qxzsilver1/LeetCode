class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: -len(x))
        word_index = {}

        for i, word, in enumerate(words):
            word_index[word] = i
        
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1

            for j in range(len(words[i])):
                w = words[i]
                predecessor = w[:j] + w[j+1:]

                if predecessor in word_index:
                    res = max(res, 1 + dfs(word_index[predecessor]))

            dp[i] = res

            return res
        
        for i in range(len(words)):
            dfs(i)
        
        return max(dp.values())
