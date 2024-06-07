class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)

        l, r = 0, 0
        prefix_index = -1

        while r < len(word):
            if word[r] == ch:
                prefix_index = r
                break
            
            r += 1
        
        while prefix_index != -1 and l < prefix_index:
            word[l], word[prefix_index] = word[prefix_index], word[l]
            l += 1
            prefix_index -= 1
        
        return ''.join(word)
        
