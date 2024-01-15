class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        output = 0

        for word in words:
            curr_word = defaultdict(int)
            good = True

            for c in word:
                curr_word[c] += 1

                if c not in chars_count or curr_word[c] > chars_count[c]:
                    good = False
                    break
            
            if good:
                output += len(word)
        
        return output
