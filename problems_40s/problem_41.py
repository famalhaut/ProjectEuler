from common.primes import miller_rabin_test
from itertools import permutations

max_pr = 0
flag = False
for pw in range(8, 0, -1):
    for permut in permutations(range(1, pw + 1)):
        num = 0
        for i in permut:
            num *= 10
            num += i
        if miller_rabin_test(num):
            max_pr = max(max_pr, num)
            flag = True
    if flag:
        break

print(max_pr)