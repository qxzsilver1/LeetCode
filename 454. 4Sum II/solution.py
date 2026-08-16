class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def sumCount(lsts: List[List[int]]) -> Counter:
            res = Counter({0: 1})

            for lst in lsts:
                tmp = Counter()

                for a in lst:
                    for total in res:
                        tmp[total + a] += res[total]

                res = tmp
            
            return res
        
        lsts = [nums1, nums2, nums3, nums4]

        k = len(lsts)

        l, r = sumCount(lsts[:k // 2]), sumCount(lsts[k // 2:])

        return sum(l[s] * r[-s] for s in l)
