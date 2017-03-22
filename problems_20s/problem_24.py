"""
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


from operator import mul
from functools import reduce


def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return reduce(mul, range(1, x + 1))


def problem(ls, n):
    result= []
    for i in range(len(ls) - 1, 0, -1):
        fct = factorial(i)
        idx = (n - 1) // fct
        n -= idx * fct
        result.append(ls.pop(idx))
    result.append(ls[0])
    return result


if __name__ == '__main__':
    objs = list(range(10))
    ans = ''.join(map(str, problem(objs, 10**6)))
    print('Answer:', ans)
