"""
Consecutive prime sum
Problem 50 
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, 
and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from common.primes import primes_gen, miller_rabin_test


def problem(limit):
    pr_gen = primes_gen()
    sum_primes = 0
    primes = []
    while sum_primes < limit:
        prime = next(pr_gen)
        sum_primes += prime
        primes.append(prime)

    length = len(primes)
    while True:
        num = sum(primes[:length])
        start = 0
        while num < limit:
            if miller_rabin_test(num):
                if length >= 3:
                    print('{} = {} + {} + ... + {}'.
                          format(num, primes[start], primes[start + 1], primes[start + length - 1]))
                else:
                    print('{} = {}'.format(num, ' + '.join(map(str, primes[start:start + length]))))

                print('The longest sum of consecutive primes below {} that adds to a prime, '
                      'contains {} terms, and is equal to {}.'.format(limit, length, num))
                return num
            else:
                if (start + length) >= len(primes):
                    primes.append(next(pr_gen))
                num += primes[start + length] - primes[start]
                start += 1
        length -= 1


if __name__ == '__main__':
    for lim in [100, 1000, 10 ** 6]:
        print('Answer:', problem(lim))
        print()
