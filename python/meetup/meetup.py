import calendar
from datetime import date

days = list(calendar.day_name)
def meetup_day(year, month, day_of_the_week, which):
    day_index = days.index(day_of_the_week)
    dates = [
        week[day_index]
        for week in calendar.monthcalendar(year, month)
        if week[day_index]]
    if which == 'teenth':
        for day_num in dates:
            if 13 <= day_num <= 19:
                return date(year, month, day_num)
    elif which == 'last':
        day_index = -1
    elif which == 'first':
        day_index = 0
    else:
        day_index = int(which[0]) - 1
    return date(year, month, dates[day_index])
