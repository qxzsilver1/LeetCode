class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        ctr = 0

        l, r = 0, len(people) - 1

        while l <= r: 
            remaining = limit - people[r]
            r -= 1
            ctr += 1

            if l <= r and remaining >= people[l]:
                l += 1
        
        return ctr
