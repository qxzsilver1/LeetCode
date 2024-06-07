class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt_dict = Counter(s)

        for i, c in enumerate(s):
            if cnt_dict[c] == 1:
                return i
        
        return -1
