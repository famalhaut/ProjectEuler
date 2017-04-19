"""
Distinct primes factors
Problem 47 
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
"""
from common.primes import factorization, primes_gen
import functools

prs_gen = primes_gen()
primes = [next(prs_gen), ]


def pretty_input(x):
    fact = ' * '.join('{}^{}'.format(pr, pw) for pr, pw in sorted(factorization(x).items()))
    return '{} = {}'.format(x, fact)


@functools.lru_cache(maxsize=None)
def factorization(x):
    for i, prime in enumerate(primes, start=1):
        if prime ** 2 > x:
            return {x: 1}
        if x % prime == 0:
            x //= prime
            result = factorization(x).copy()
            if prime in result:
                result[prime] += 1
            else:
                result[prime] = 1
            return result
        if i == len(primes):
            primes.append(next(prs_gen))


def problem():
    num = 3 * 5 * 7
    while True:
        if ((num % 2 == 0 and len(factorization(num)) == 4 and len(factorization(num + 1)) == 3) or
                (num % 2 == 1 and len(factorization(num)) == 3 and len(
                    factorization(num + 1)) == 4)):
            if len(factorization(2 * num + 1)) == 4:
                if len(factorization(2 * num - 1)) == 4:
                    for i in range(2 * num - 1, 2 * num + 3):
                        print(pretty_input(i))
                    return 2 * num - 1
                elif len(factorization(2 * num + 3)) == 4:
                    for i in range(2 * num, 2 * num + 4):
                        print(pretty_input(i))
                    return 2 * num
                else:
                    num += 2

            else:
                num += 1
        else:
            num += 1


if __name__ == '__main__':
    print('Answer:', problem())
