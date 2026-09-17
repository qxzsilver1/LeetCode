class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        word_cnt = 0

        for m in message:
            if m in banned:
                word_cnt += 1
            else:
                continue
            
            if word_cnt >= 2:
                return True
        
        return word_cnt >= 2
            
