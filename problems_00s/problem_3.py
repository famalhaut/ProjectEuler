"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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
    result = x
    for p in primes_gen():
        # print('новое p', x, p)
        if p * p > x:
            if x == 1:
                return result
            else:
                return x
        while x % p == 0:
            # print('круг', x, p)
            x //= p
            result = p


if __name__ == '__main__':
    print('Test:', problem(13195))
    print('Answer:', problem(600851475143))
