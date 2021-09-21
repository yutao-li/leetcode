class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(2, 13):
            months[i] += months[i - 1]

        def f(date):
            y, m, d = map(int, date.split('-'))
            return 365 * (y - 1) + months[m - 1] + d + (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400 + (m > 2 and (
                    y % 4 == 0 and y % 100 != 0 or y % 400 == 0))

        return abs(f(date1) - f(date2))


res = Solution().daysBetweenDates(date1="2020-01-15", date2="2019-12-31")

