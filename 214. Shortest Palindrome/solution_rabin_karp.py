class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix_hash, suffix_hash = 0, 0
        base = 29
        power = 1

        MOD = 10 ** 9 + 7

        last_idx = 0 # -1

        for i, c in enumerate(s):
            char = (ord(c) - ord('a')) + 1

            prefix_hash = (prefix_hash * base) % MOD
            prefix_hash = (prefix_hash + char) % MOD

            suffix_hash = (suffix_hash + char * power) % MOD
            power = (power * base) % MOD

            if suffix_hash == prefix_hash:
                last_idx = i

        suffix_hash = s[last_idx + 1:]
        
        return suffix_hash[::-1] + s
