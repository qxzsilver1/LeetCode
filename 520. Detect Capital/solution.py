class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_is_capital = True if word[0].isupper() else False

        for i in range(1, len(word)):
            if word[i-1].isupper() and word[i].isupper() or word[i-1].islower() and word[i].islower():
                continue
            elif i == 1 and first_is_capital:
                continue
            else:
                return False
        
        return True
