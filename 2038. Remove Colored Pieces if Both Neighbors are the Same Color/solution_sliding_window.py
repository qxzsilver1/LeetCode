class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0
        l, r = 0, 0

        while r < len(colors):
            if colors[l] != colors[r]:
                l = r
            
            extra_chars = r - l + 1 - 2

            if extra_chars > 0:
                if colors[r] == 'A':
                    alice += 1
                
                if colors[r] == 'B':
                    bob += 1
            
            r += 1


        return alice > bob
