import datetime

def f_re(year, month, num):
    F = 0
    day_li = [31, F, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 0 <= num <= 31:
        return (year, month, num)
    else:
        if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
            F = 29
            day_li[1] = F
            for j in range(12):
                if num > day_li[j]:
                    num -= day_li[j]
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
                    break
            return f_re(year, month, num)
        else:
            F = 28
            day_li[1] = F
            for j in range(12):
                if num > day_li[j]:
                    num -= day_li[j]
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
                    break
            return f_re(year, month, num)

def f(year, month, day, num):
    num += day
    if 0 <= num <= 31:
        return (year, month, num)
    else:
        return f_re(year, month, num)


def date(year, month, day):
    week_li = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    given_date = datetime.datetime(year, month, day)
    what_date_num = given_date.weekday()
    what_date_name = week_li[what_date_num]
    return what_date_name


year, month, day, num = map(int, input().split())
result = f(year, month, day, num)
print(result[0], "년", result[1], "월", result[2], "일", date(result[0], result[1], result[2]))
