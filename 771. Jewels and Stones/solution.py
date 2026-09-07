class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_char_map = [0] * 52 # maps A-Z then a-z for each 26 letters

        res = 0

        for j in jewels:
            pos = ord(j) - ord('A') if ord(j) - ord('A') <= 25 else ord(j) - ord('a') + 26
            jewels_char_map[pos] = 1
        
        for s in stones:
            if ord(s) - ord('A') <= 25:
                if jewels_char_map[ord(s) - ord('A')] == 1:
                    res += 1
                else:
                    continue
            else:
                if jewels_char_map[ord(s) - ord('a') + 26] == 1:
                    res += 1
                else:
                    continue
        
        return res
