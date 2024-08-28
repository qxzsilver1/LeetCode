class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def rotateByB(s, b):
            s = list(s)
            return ''.join(s[b:] + s[:b])
        
        def addAToOdd(s, a):
            s = list(s)
            for i in range(1, len(s), 2):
                s[i] = str((int(s[i]) + a) % 10)
            
            return ''.join(s)
        
        def addAToEven(s, a):
            s = list(s)
            for i in range(0, len(s), 2):
                s[i] = str((int(s[i]) + a) % 10)
            
            return ''.join(s)
        
        def gcd(a, b):
            return b if not a % b else gcd(b, a % b)

        res = s

        a_cycle = 10 // gcd(10 ,a)
        b_cycle = len(s) // gcd(len(s), b)

        curr_s = s

        if b % 2 == 0:
            for i in range(1, a_cycle + 1):
                curr_s = addAToOdd(curr_s, a)

                for j in range(1, b_cycle + 1):
                    curr_s = rotateByB(curr_s, b)

                    if curr_s < res:
                        res = curr_s
        else:
            for i in range(1, a_cycle + 1):
                curr_s = addAToOdd(curr_s, a)
                
                for k in range(1, a_cycle + 1):
                    curr_s = addAToEven(curr_s, a)

                    for j in range(1, b_cycle + 1):
                        curr_s = rotateByB(curr_s, b)

                        if curr_s < res:
                            res = curr_s

        return res
