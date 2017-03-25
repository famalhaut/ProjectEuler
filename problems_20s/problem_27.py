"""
Quadratic primes
Problem 27
Euler discovered the remarkable quadratic formula: n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40, 40^2+40+41=40(40+1)+41 is divisible by 41, and
certainly when n=41, 41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the
consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n=0.
"""
from common.primes import miller_rabin_test
from math import floor


def quadratic(x, a, b):
    return x ** 2 + a * x + b


def problem():
    max_num_primes, possible_a, possible_b = 0, 0, 0
    for b in range(2, 1001):
        if miller_rabin_test(b):
            endpoint = floor(b ** 0.5)
            for a in range(-2 * endpoint, 2 * endpoint + 1, 1):
                num_primes = 0
                for n in range(0, b):
                    if miller_rabin_test(quadratic(n, a, b)):
                        num_primes += 1
                    else:
                        break
                if num_primes > max_num_primes:
                    possible_a = a
                    possible_b = b
                    max_num_primes = num_primes
    return possible_a, possible_b, max_num_primes


if __name__ == '__main__':
    a, b, num_primes = problem()
    print('n ^ 2 + ({a}) * n + ({b}) will produce {num_primes} primes for the consecutive '
          'integer values 0 <= n < {num_primes}.'.format(a=a, b=b, num_primes=num_primes))
    print('Answer:', a * b)
