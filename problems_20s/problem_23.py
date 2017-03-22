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

list_primes = []
for prime in primes_gen():
    list_primes.append(prime)
    if prime > 28123 // 2:
        break


def factorization(x):
    if x == 1:
        return {1: 1}
    result = {}
    for p in list_primes:
        if p * p > x:
            if x > 1:
                result[x] = 1
                return result
            else:
                return result

        while x % p == 0:
            x //= p
            if p in result:
                result[p] += 1
            else:
                result[p] = 1

st_res = time()
st = time()
abundant_nums = set()
abundant_sums = set()
for num in range(2, 28123):
    # print('test', num)
    sum_divs = 1
    for prime, pw in factorization(num).items():
        # print(prime, pw)
        sum_divs *= (prime ** (pw + 1) - 1) // (prime - 1)
    if sum_divs > 2 * num:
        abundant_nums.add(num)
        for abundant_num in abundant_nums:#filter(lambda x: num + x < 28123, abundant_nums):
            abundant_sums.add(num + abundant_num)
    # print('-'*20)
print(len(abundant_nums))
print('qw', time() - st)

# st_res = time()
# sums = set()
# for i in abundant_nums:
#     for j in filter(lambda x: x < 28123 - i, abundant_nums):
#         sums.add(i + j)
# print('qqq', time() - st)

def problem():
    return sum(set(range(1, 28123)) - abundant_sums)

if __name__ == '__main__':
    print('Answer:', problem())
    print(time() - st_res)
