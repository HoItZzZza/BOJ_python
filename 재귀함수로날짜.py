import datetime

def f(year, month, day, num):
    if 0 <= num <= 31:
        return (year, month, day)
    else:
        F = 0
        day_li = [31, F, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        num += day

        if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
            F = 29
            for j in range(12):
                if num > day_li[j]:
                    num -= day_li[j]
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
            day = 0
            return f(year, month, day, num)
        else:
            F = 28
            for j in range(12):
                if num > day_li[j]:
                    num -= day_li[j]
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
            day = 0
            return f(year, month, day, num)


def date(year, month, day):
    week_li = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    given_date = datetime.datetime(year, month, day)
    what_date_num = given_date.weekday()
    what_date_name = week_li[what_date_num]
    return what_date_name


year, month, day, num = map(int, input().split())
result = f(year, month, day, num)
print(result[0], "년", result[1], "월", result[2], "일", date(year, month, day))
