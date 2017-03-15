"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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


def problem(x):
    result = 0
    primes = primes_gen().__iter__()
    prime = primes.__next__()
    while prime < x:
        result += prime
        prime = primes.__next__()
    return result


if __name__ == '__main__':
    print('Test:', problem(10))
    print('Answer:', problem(2 * 10 ** 6))
