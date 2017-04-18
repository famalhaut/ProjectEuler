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
from time import time
import functools

@functools.lru_cache(10)
def foo(x, q=None):
    amount = 0
    if x == 1:
        return False
    for p in primes_gen():
        if p * p > x:
            if x == 1:
                return amount == q
            else:
                return (amount + 1) == q
        if x % p == 0:
            amount += 1
            if amount > q:
                return False
        while x % p == 0:
            x //= p
#######################################################################################

# st = time()
# i = 14
# while True:
#
#     if len(factorization(i)) == 4:
#         if len(factorization(i + 1)) == 4:
#             if len(factorization(i + 2)) == 4:
#                 if len(factorization(i + 3)) == 4:
#                     print(sorted(factorization(i + 0).items()))
#                     print(sorted(factorization(i + 1).items()))
#                     print(sorted(factorization(i + 2).items()))
#                     print(sorted(factorization(i + 3).items()))
#                     print(i)
#                     break
#                 else:
#                     i += 4
#             else:
#                 i += 3
#         else:
#             i += 2
#     else:
#         i += 1
# print(time() - st)


############################################################################################

@functools.lru_cache(10)
def factorization2(x):
    return factorization(x)


st = time()
i = 3 * 5 * 7
while True:

    fact_i0 = factorization2(i)
    fact_i1 = factorization2(i + 1)

    if (i % 2 == 0 and len(fact_i0) == 4 and len(fact_i1) == 3) or \
            (i % 2 == 1 and len(fact_i0) == 3 and len(fact_i1) == 4):
        if len(factorization2(2 * i + 1)) == 4:
            if len(factorization2(2 * i - 1)) == 4:
                print('-1')

                print(fact_i0, fact_i1)

                print(sorted(factorization2(2 * i - 1).items()))
                print(sorted(factorization2(2 * i + 0).items()))
                print(sorted(factorization2(2 * i + 1).items()))
                print(sorted(factorization2(2 * i + 2).items()))

                print(2 * i - 1)
                break
            elif len(factorization2(2 * i + 3)) == 4:
                print('+3')
                print(fact_i0, fact_i1)
                print(sorted(factorization2(2 * i + 0).items()))
                print(sorted(factorization2(2 * i + 1).items()))
                print(sorted(factorization2(2 * i + 2).items()))
                print(sorted(factorization2(2 * i + 3).items()))

                print(2 * i)
                break
            else:
                i += 2

        else:
            i += 1
    else:
        i += 1

print(time() - st)


##################################################################################################

st = time()
i = 3 * 5 * 7
while True:

    if (i % 2 == 0 and foo(i, 4) and foo(i + 1, 3)) or \
            (i % 2 == 1 and foo(i, 3) and foo(i + 1, 4)):
        if foo(2 * i + 1, 4):
            if foo(2 * i - 1, 4):
                print('-1')

                print(sorted(factorization2(2 * i - 1).items()))
                print(sorted(factorization2(2 * i + 0).items()))
                print(sorted(factorization2(2 * i + 1).items()))
                print(sorted(factorization2(2 * i + 2).items()))

                print(2 * i - 1)
                break
            elif foo(2 * i + 3, 4):
                print('+3')

                print(sorted(factorization2(2 * i + 0).items()))
                print(sorted(factorization2(2 * i + 1).items()))
                print(sorted(factorization2(2 * i + 2).items()))
                print(sorted(factorization2(2 * i + 3).items()))

                print(2 * i)
                break
            else:
                i += 2

        else:
            i += 1
    else:
        i += 1

print(time() - st)
