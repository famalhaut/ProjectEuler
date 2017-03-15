"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def problem(x):
    for a in range(1, x):
        for b in range(a + 1, (1000 - a) // 2 + 1):
            c = x - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return 'a = {}, b = {}, c = {}, abc = {}'.format(a, b, c, a * b * c)


if __name__ == '__main__':
    print('Test:', problem(12))
    print('Answer:', problem(1000))
