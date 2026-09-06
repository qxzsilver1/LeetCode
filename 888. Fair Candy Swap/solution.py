class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total, bob_total = sum(aliceSizes), sum(bobSizes)

        bob_set = set(bobSizes)

        for a in aliceSizes:
            if a + (bob_total - alice_total) // 2 in bob_set:
                return [a, a + (bob_total - alice_total) // 2]
