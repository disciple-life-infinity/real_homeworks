# ---------------------------------------1---------------------------------------------
#
# date = datetime.date.today()
# dw = datetime.date.weekday(date)
# print(dw)

# ---------------------------------------2---------------------------------------------
# import calendar
# from datetime import datetime
# now = datetime.now()
#
# current_year = now.year
# current_month = now.month
#
# cal = calendar.TextCalendar()
#
#
# one_month_calendar = cal.formatmonth(current_year, current_month)
# one_year_calendar = cal.formatyear(current_year)
#
# print("1-oylik kalendar:\n")
# print(one_month_calendar)
# print("1-yillik kalendar:\n")
# print(one_year_calendar)
#
# ------------------------------------------3-----------------------------------------
# def big_date(date1, date2):
#     dt1 = datetime.strptime(date1, '%Y-%m-%d')
#     dt2 = datetime.strptime(date2, '%Y-%m-%d')
#
#     if dt1 > dt2:
#         return date1
#     else:
#         return date2
#
# print(big_date('2024-06-13', '2023-12-25'))
# print(big_date('2023-01-01', '2023-01-01'))
# print(big_date('2022-05-15', '2022-05-16'))

# ------------------------------------------4-----------------------------------------

import time

current_time = time.localtime()

formatted_time_1 = time.strftime("%A %d %B %Y %H:%M:%S", current_time)
formatted_time_2 = time.strftime("%d.%m.%Y", current_time)
print("Today:")
print(formatted_time_1)
print(formatted_time_2)

# ------------------------------------------5-----------------------------------------

# cal = calendar.HTMLCalendar()
#
# year = 2023
# html_calendar = '<html><body><h1>Calendar for {}</h1>'.format(year)
#
# for month in range(1, 13):
#     html_calendar += '<h2>{}</h2>'.format(calendar.month_name[month])
#     html_calendar += cal.formatmonth(year, month)
#
# html_calendar += '</body></html>'
#
# with open('calendar_2023.html', 'w') as file:
#     file.write(html_calendar)
#
# print(html_calendar)
