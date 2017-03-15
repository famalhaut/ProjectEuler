"""
Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def problem(x):
    return sum(map(int, str(x)))


if __name__ == '__main__':
    print('Test:', problem(2 ** 15))
    print('Answer:', problem(2 ** 1000))
