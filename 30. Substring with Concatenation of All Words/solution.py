class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)

        word_len = len(words[0])
        substring_len = word_len * k

        word_count = Counter(words)

        def slidingWindow(left):
            words_found = defaultdict(int)
            words_used = 0
            excess_word = False

            for right in range(left, n, word_len):
                if right + word_len > n:
                    break
                
                sub = s[right:right + word_len]

                if sub not in word_count:
                    words_found = defaultdict(int)
                    words_used = 0
                    excess_word = False

                    left = right + word_len
                else:
                    while right - left == substring_len or excess_word:
                        leftmost_word = s[left:left + word_len]
                        left += word_len
                        words_found[leftmost_word] -= 1
                    
                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            excess_word = False
                        else:
                            words_used -= 1
                    
                    words_found[sub] += 1

                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        excess_word = True
                    
                    if words_used == k and not excess_word:
                        res.append(left)
        
        res = []

        for i in range(word_len):
            slidingWindow(i)
        
        return res
