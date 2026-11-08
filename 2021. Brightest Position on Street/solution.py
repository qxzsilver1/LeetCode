class Solution:
    def brightestPosition(self, lights: list[list[int]]) -> int:
        diff = defaultdict(int)

        for pos, rng in lights:
            start, end = pos - rng, pos + rng
            diff[start] += 1
            diff[end + 1] -= 1

        max_bright = curr = 0
        res = 0

        for key in sorted(diff):
            curr += diff[key]

            if curr > max_bright:
                max_bright = curr
                res = key
        
        return res
