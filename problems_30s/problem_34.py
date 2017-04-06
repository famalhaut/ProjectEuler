"""
Digit factorials
Problem 34 
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

facts = {}
for i in range(10):
    facts[i] = factorial(i)


def get_max_possible_num():
    order = 1
    while 10 ** order - 1 < order * facts[9]:
        order += 1
    return order * factorial(9)


def problem():
    result = 0

    for num in range(10, get_max_possible_num()):
        s = 0
        temp = num
        while temp > 0:
            s += facts[temp % 10]
            temp //= 10
            if s > num:
                break
        else:
            if num == s:
                print(num, '=', ' + '.join(map(lambda ch: ch + '!', str(num))))
                result += num
    return result


if __name__ == '__main__':
    print('Answer:', problem())
