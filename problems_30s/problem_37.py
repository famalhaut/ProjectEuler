"""
Truncatable primes
Problem 37 
The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly 
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and 
right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from common.primes import miller_rabin_test


def problem():
    truncatable = []

    def check(xs):

        probables = []

        for x in xs:
            for i in range(1, 10):
                new_x = int(str(i) + str(x))
                if miller_rabin_test(new_x):

                    probables.append(new_x)

                    pow_10 = 10
                    while pow_10 < new_x:
                        if miller_rabin_test(new_x // pow_10):
                            pow_10 *= 10
                        else:
                            break
                    else:
                        truncatable.append(new_x)
        if len(truncatable) < 11:
            check(probables)

    check([2, 3, 5, 7])

    return truncatable


if __name__ == '__main__':
    print('Answer:', sum(problem()))
