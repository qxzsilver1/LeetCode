class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_ablno_count = [1, 1, 2, 1, 2]
        ctr = 0

        def balloon_counter(char):
            if char == 'a':
                balloon_ablno_count[0] -= 1
            elif char == 'b':
                balloon_ablno_count[1] -= 1
            elif char == 'l':
                balloon_ablno_count[2] -= 1
            elif char == 'n':
                balloon_ablno_count[3] -= 1
            elif char == 'o':
                balloon_ablno_count[4] -= 1

        for t in text:
            balloon_counter(t)

            if all(cnt == 0 for cnt in balloon_ablno_count):
                ctr += 1
                balloon_ablno_count = [1, 1, 2, 1, 2]

        return ctr
