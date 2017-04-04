"""
Digit cancelling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling
the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and
containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the
denominator.
"""


def gcd(x, y):
    if x <= y:
        x, y = y, x

    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def problem():
    up = 1
    down = 1

    # x = (10a + b) / (10c + b)
    for a in range(1, 10):
        for c in range(a + 1, 10):

            b = c
            for d in range(1, 10):
                if a * (10 * c + d) == d * (10 * a + b):
                    print('{}/{}'.format(10 * a + b, 10 * c + d))
                    up *= 10 * a + b
                    down *= 10 * c + d

            d = a
            for b in range(1, 10):
                if b * (10 * c + d) == c * (10 * a + b):
                    print('{}/{}'.format(10 * a + b, 10 * c + d))
                    up *= 10 * a + b
                    down *= 10 * c + d
    return up, down


if __name__ == '__main__':
    m, n = problem()
    print('Answer:', n / gcd(m, n))
