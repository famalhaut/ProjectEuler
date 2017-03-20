"""
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal
to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown
that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from common.primes import primes_gen
from time import time

primes = []
for pr in primes_gen():
    primes.append(pr)
    if pr > 28123 // 2:
        break
set_primes = set(primes)


def factorization(x):
    if x == 1:
        return {1: 1}
    result = {}
    # TODO Каждый раз по новой создаём список простых.
    for p in primes:
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

st = time()
abundant_nums = []
for num in range(2, 28123):
    # print(num)
    divs = {1}
    for pr, pw in factorization(num).items():
        new_divs = set()
        for div in divs:
            for i in range(pw + 1):
                new_divs.add(div * pr ** i)
        divs.update(new_divs)
        # print(divs, new_divs)
    if sum(divs) > 2 * num:
        abundant_nums.append(num)
    # print('-'*20)
print(len(abundant_nums))
print('qw', time() - st)


st = time()
abundant_nums = []
for num in range(2, 15):
    # print(num)
    sum_divs = 1
    for pr, pw in factorization(num).items():
        sum_divs *= (pr ** (pw + 1)) // (pr - 1)
    if sum_divs > 2 * num:
        abundant_nums.append(num)
    # print('-'*20)
print(abundant_nums)
print('qw', time() - st)


sums = set()
for i in abundant_nums:
    for j in abundant_nums:
        sums.add(i + j)


def problem():
    return sum(set(range(1, 28123)) - sums)

if __name__ == '__main__':
    print('Answer:', problem())
