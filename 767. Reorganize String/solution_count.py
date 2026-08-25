class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord("a")] += 1

        max_freq = max(freq)

        if max_freq > (len(s) + 1) // 2:
            return ""

        res = []

        while len(res) < len(s):
            max_idx = freq.index(max(freq))
            char = chr(max_idx + ord("a"))
            
            res.append(char)
            freq[max_idx] -= 1

            if freq[max_idx] == 0:
                continue

            tmp = freq[max_idx]
            freq[max_idx] = float("-inf")
            
            nextmax_idx = freq.index(max(freq))
            char = chr(nextmax_idx + ord("a"))
            res.append(char)
            
            freq[max_idx] = tmp
            freq[nextmax_idx] -= 1

        return "".join(res)
