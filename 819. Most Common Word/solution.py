class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        count_dict = defaultdict(int)
        max_count, max_word = 0, ''

        word_list = filter(None, re.split(r"[ !?',;.]+", paragraph))
        word_list = [x.lower() for x in word_list]

        for word in word_list:
            
            if word not in banned:
                count_dict[word] += 1

                if count_dict[word] > max_count:
                    max_count = count_dict[word]
                    max_word = word

        
        return max_word
