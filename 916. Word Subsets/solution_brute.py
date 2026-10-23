class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        res = []
        for w1 in words1:
            count1 = Counter(w1)
            is_subset = True

            for w2 in words2:
                count2 = Counter(w2)
                for c in count2:
                    if count2[c] > count1[c]:
                        is_subset = False
                        break

                if not is_subset: break

            if is_subset:
                res.append(w1)

        return res
