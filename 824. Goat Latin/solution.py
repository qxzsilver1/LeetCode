class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        word_list = sentence.split()
        vowels_set = set(['a', 'e', 'i', 'o', 'u'])

        for i in range(len(word_list)):
            if word_list[i][0].lower() in vowels_set:
                word_list[i] += 'ma'
            else:
                word_list[i] = word_list[i][1:] + word_list[i][0] + 'ma'
            
            word_list[i] += 'a' * (i + 1)
        
        return ' '.join(word_list)
