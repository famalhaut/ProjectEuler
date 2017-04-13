"""
Pandigital prime
Problem 41 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly 
once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from common.primes import miller_rabin_test
from itertools import permutations


def problem():
    max_prime = 0
    flag = False
    # 1 + 2 + ... + 9 = 45, 45 % 3 => 9-digit pandigital is not prime.
    for pw in range(8, 0, -1):
        for permut in permutations(range(1, pw + 1)):
            num = 0
            for i in permut:
                num *= 10
                num += i
            if miller_rabin_test(num):
                max_prime = max(max_prime, num)
                flag = True
        if flag:
            break

    return max_prime


if __name__ == '__main__':
    print('Answer:', problem())
