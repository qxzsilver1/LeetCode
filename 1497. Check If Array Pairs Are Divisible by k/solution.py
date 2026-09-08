class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = defaultdict(int)

        for i in arr:
            remainders[(i % k + k)  % k] += 1
        
        for i in arr:
            rem = (i % k + k) % k

            if rem == 0:
                if remainders[rem] % 2 == 1:
                    return False
            elif remainders[rem] != remainders[k - rem]:
                return False
        
        return True
