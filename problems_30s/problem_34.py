from math import factorial
from time import time

#
# for a in range(1, 10):
#     print(a, 10 ** a - 1 > factorial(9) * a)

facts = {}
for i in range(10):
    facts[i] = factorial(i)


def problem():
    result = 0

    c = 1
    while 10 ** c - 1 < c * facts[9]:
        c += 1

    for num in range(10, c * factorial(9)):
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
