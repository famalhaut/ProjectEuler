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
    result = {}
    if x == 1:
        return {1: 1}
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

d = {}
result = 0
for num in range(3, 10000):
    temp = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            temp += i
    d[num] = temp
    if num not in d:

    else:
        result += num
