"""
Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the 
sum of a prime and  .

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from common.primes import primes_gen


def problem():
    num = 3
    primes = set()
    for prime in primes_gen():
        primes.add(prime)
        while num < prime:
            n, twice_square = 1, 2
            while twice_square < num:
                if (num - twice_square) in primes:
                    break
                twice_square += 4 * n + 2
                n += 1
            else:
                return num
            num += 2
        num = prime + 2


if __name__ == '__main__':
    print('Answer:', problem())
