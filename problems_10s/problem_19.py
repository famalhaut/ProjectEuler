"""
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is
divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date


def days_in_month(month, year):
    if month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                return 28
            return 29
        return 28
    else:
        return 31


def problem():
    month = 1
    year = 1900
    weekday = 0
    result = 0
    while year < 2001:
        if weekday == 6 and year >= 1901:
            result += 1
        weekday = (weekday + days_in_month(month, year)) % 7
        month += 1
        if month > 12:
            month = 1
            year += 1
    return result


def simple_solution():
    result = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if date(year, month, 1).isoweekday() == 7:
                result += 1
    return result


if __name__ == '__main__':
    print('Test:', simple_solution())
    print('Answer:', problem())
