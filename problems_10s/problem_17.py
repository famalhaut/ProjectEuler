"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def get_num_word(x):
    base = {0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'}
    if 0 <= x <= 9:
        return base[x]
    elif 10 <= x <= 12:
        d = {10: 'ten',
             11: 'eleven',
             12: 'twelve'}
        return d[x]
    elif 13 <= x <= 19:
        exception = {13: 'thir',
                     15: 'fif',
                     18: 'eigh'}
        return exception.get(x, base.get(x % 10)) + 'teen'
    elif 20 <= x <= 99:
        exception = {20: 'twen',
                     30: 'thir',
                     40: 'for',
                     50: 'fif',
                     80: 'eigh'}
        temp = exception.get(x - x % 10, base[x // 10]) + 'ty'
        if x % 10 != 0:
            temp += '-' + base[x % 10]
        return temp
    elif 100 <= x <= 999:
        temp = base[x // 100] + ' hundred'
        if x % 100 != 0:
            temp += ' and ' + get_num_word(x % 100)
        return temp
    elif 1000 <= x <= 9999:
        temp = base[x // 1000] + ' thousand'
        if x % 1000 != 0:
            temp += ' and ' + get_num_word(x % 1000)
        return temp


def problem():
    result = 0
    for num in range(1, 1001):
        result += len(get_num_word(num).replace(' ', '').replace('-', ''))
    return result


if __name__ == '__main__':
    print('Answer:', problem())
