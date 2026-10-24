class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        prefix_sum_days = [0]

        for days in days_in_month:
            prefix_sum_days.append(prefix_sum_days[-1] + days)

        def calculateDayOfYear(date):
            month = int(date[:2])
            day = int(date[3:])

            return prefix_sum_days[month - 1] + day
        
        alice_days = [calculateDayOfYear(arriveAlice), calculateDayOfYear(leaveAlice)]
        bob_days = [calculateDayOfYear(arriveBob), calculateDayOfYear(leaveBob)]

        return max(0, min(alice_days[1], bob_days[1]) - max(alice_days[0], bob_days[0]) + 1)
