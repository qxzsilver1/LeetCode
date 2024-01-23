class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if all(i == suits[0] for i in suits):
            return 'Flush'
        
        card_dict = Counter(ranks)

        if max(card_dict.values()) >= 3:
            return 'Three of a Kind'
        elif max(card_dict.values()) == 2:
            return 'Pair'
        else:
            return 'High Card'
