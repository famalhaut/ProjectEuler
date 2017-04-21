from common.primes import primes_gen
from collections import Counter
from itertools import combinations
from time import time

st = time()
res = {}
flag = False
for prime in primes_gen():
    digits = list(map(int, str(prime)))
    for digit, count in Counter(digits).items():
        if count > 2:
            for positions in combinations([n for n, d in enumerate(digits) if d == digit], 3):
                x = tuple((d if j not in positions else '*') for j, d in enumerate(digits))
                if x not in res:
                    res[x] = {prime}
                else:
                    res[x].add(prime)
                    if len(res[x]) == 8:
                        print(x)
                        print(res[x])
                        print(min(res[x]))
                        flag = True
    if flag:
        break
print(time() - st)
