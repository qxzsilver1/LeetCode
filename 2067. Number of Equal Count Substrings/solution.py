class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        res = 0

        for distinct in range(1, 27):
            width = distinct * count
            
            if width > len(s): break
            
            freq = [0] * 26
            exact = 0
            
            for i, ch in enumerate(s):
                x = ord(ch) - 97
                exact -= freq[x] == count
                freq[x] += 1
                exact += freq[x] == count
                
                if i >= width:
                    x = ord(s[i - width]) - 97
                    exact -= freq[x] == count
                    freq[x] -= 1
                    exact += freq[x] == count
                
                if i + 1 >= width and exact == distinct: res += 1
        return res
