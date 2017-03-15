"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def check(x, list_primes):
    for prime in list_primes:
        if x % prime == 0:
            return False
        else:
            if prime * prime > x:
                return True


def primes_gen():
    primes = [2, 3]
    yield 2
    yield 3
    multiple_6 = 6
    while True:
        for possible in [multiple_6 - 1, multiple_6 + 1]:
            if check(possible, primes):
                primes.append(possible)
                yield possible
        multiple_6 += 6


def factorization(x):
    result = {}
    if x == 1:
        return {1: 1}
    # TODO Каждый раз по новой создаём список простых.
    for p in primes_gen():
        if p * p > x:
            if x == 1:
                return result
            else:
                result[x] = 1
                return result
        while x % p == 0:
            x //= p
            if p in result:
                result[p] += 1
            else:
                result[p] = 1


def problem(x):
    mlt_set = {}
    for i in range(2, x + 1):
        for pr, power in factorization(i).items():
            if pr in mlt_set:
                mlt_set[pr] = max(power, mlt_set[pr])
            else:
                mlt_set[pr] = power
    result = 1
    for pr, power in mlt_set.items():
        result *= pr ** power
    return result


if __name__ == '__main__':
    print('Test:', problem(10))
    print('Answer:', problem(20))
