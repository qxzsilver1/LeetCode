class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        word_set = set([''])
        res = ''

        for word in words:
            if word[:-1] in word_set:
                if len(word) > len(res):
                    res = word
                word_set.add(word)

        return res
