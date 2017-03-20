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
    if x == 1:
        return {1: 1}
    result = {}
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


# Deterministic variants Miller-Rabin primality test.
# for n < 3,317,044,064,679,887,385,961,981
def miller_rabin_test(n):
    assert (2 <= n <= 3317044064679887385961981) and isinstance(n, int)
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        num = n - 1
        s = 0
        while num % 2 == 0:
            s += 1
            num //= 2
        d = num
        if n < 2047:
            list_a = [2]
        elif n < 1373653:
            list_a = [2, 3]
        elif n < 9080191:
            list_a = [31, 73]
        elif n < 25326001:
            list_a = [2, 3, 5]
        elif n < 3215031751:
            list_a = [2, 3, 5, 7]
        elif n < 4759123141:
            list_a = [2, 7, 61]
        elif n < 1122004669633:
            list_a = [2, 13, 23, 1662803]
        elif n < 2152302898747:
            list_a = [2, 3, 5, 7, 11]
        elif n < 3474749660383:
            list_a = [2, 3, 5, 7, 11, 13]
        elif n < 341550071728321:
            list_a = [2, 3, 5, 7, 11, 13, 17]
        elif n < 3825123056546413051:
            list_a = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        elif n < 18446744073709551616:
            list_a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        elif n < 318665857834031151167461:
            list_a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        elif n < 3317044064679887385961981:
            list_a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        answer = False
        for a in list_a:
            if pow(a, d, n) != 1:
                for r in range(s):
                    if pow(a, 2 ** r * d, n) == (-1) % n:
                        break
                else:
                    return False
        return True

# from time import time
#
# num_test = 10 ** 6
#
# st = time()
# pr_mr = [2]
# for i in range(3, num_test, 2):
#     if miller_rabin_test(i):
#         pr_mr.append(i)
# print(len(pr_mr))
# print('m-r',time() - st)
#
# print('-'*30)
#
# st = time()
# pr_old = []
# gen = primes_gen().__iter__()
# while True:
#     pr = gen.__next__()
#     if pr >= num_test:
#         break
#     pr_old.append(pr)
# print(len(pr_old))
# print('old', time() - st)
#
