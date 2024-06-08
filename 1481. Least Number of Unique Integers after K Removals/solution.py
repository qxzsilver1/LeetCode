class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency_map = Counter(arr)

        freq_list = [0] * (len(arr) + 1)

        for n, f in frequency_map.items():
            freq_list[f] += 1

        res = len(frequency_map)

        for f in range(1, len(freq_list)):
            removal = freq_list[f]

            if k >= f * removal:
                k -= f * removal
                res -= removal
            else:
                removal = k // f
                res -= removal
                break
        
        return res
