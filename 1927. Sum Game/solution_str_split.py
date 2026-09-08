class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        
        def get(s):
            nn, qq = 0, 0

            for c in s:
                if c == '?':
                    qq += 1
                else:
                    nn += int(c)
            return nn, qq
        
        n_first, q_first = get(num[:n // 2])
        n_second, q_second = get(num[n // 2:])

        return (q_first + q_second) % 2 == 1 or (n_first - n_second) != (q_second - q_first) * 9 // 2
