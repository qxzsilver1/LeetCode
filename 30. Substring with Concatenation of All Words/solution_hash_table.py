class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)

        word_len = len(words[0])
        substring_len = word_len * k

        word_count = Counter(words)

        def check(i):
            remaining = word_count.copy()
            words_used = 0

            for j in range(i, i + substring_len, word_len):
                sub = s[j:j + word_len]

                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break
            
            return words_used == k
        
        res = []

        for i in range(n - substring_len + 1):
            if check(i):
                res.append(i)
        
        return res
