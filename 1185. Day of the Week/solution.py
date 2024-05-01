class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        if month < 3:
            month += 12
            year -= 1
        century = year // 100
        year %= 100

        week = (century // 4 - 2 * century + year + year // 4 + 13 * (month + 1) // 5 + day - 1) % 7

        return days_of_week[week]
