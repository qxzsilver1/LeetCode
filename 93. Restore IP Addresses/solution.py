class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(s) > 12:
            return res

        def backtrack(i, num_dots, curr_IP):
            if num_dots == 4 and i == len(s):
                res.append(curr_IP[:-1])
                return

            if num_dots > 4:
                return
            
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != '0'):
                    backtrack(j+1, num_dots + 1, curr_IP + s[i:j+1] + '.')

        backtrack(0, 0, '')

        return res
