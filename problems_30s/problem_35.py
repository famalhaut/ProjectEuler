from common.primes import miller_rabin_test
from itertools import permutations

d = {}
for num in range(2, 10 ** 6):
    temp = num
    s = []
    while temp > 0:
        s.append(temp % 10)
        temp //= 10

    if not ({0, 2, 4, 6, 8, 5} & set(s)):
        q = tuple(sorted(s))
        if q not in d:
            res = True
            for permut in permutations(q):
                permut_num = 0
                for i in permut:
                    permut_num *= 10
                    permut_num += i
                if miller_rabin_test(permut_num):
                    pass
                else:
                    d[q] = False
                    break
            else:
                d[q] = True

for key, val in d.items():
    if val:
        print(key)