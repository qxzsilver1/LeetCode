class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        pref_sum = 0

        odd_cnt, even_cnt = 0, 0

        MOD = 10 ** 9 + 7

        res = 0

        for num in arr:
            pref_sum += num

            if pref_sum % 2:
                res = (res + 1 + even_cnt) % MOD
                odd_cnt += 1
            else:
                res = (res + odd_cnt) % MOD
                even_cnt += 1
        
        return res
