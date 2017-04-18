"""
Triangular, pentagonal, and hexagonal
Problem 45 
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""


def triangular(n):
    return n * (n + 1) // 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def problem():
    ps, hs = set(), set()
    i, amount, t = 1, 0, 1
    while amount < 3:
        ps.add(pentagonal(i))
        hs.add(hexagonal(i))

        t = triangular(i)
        if (t in ps) and (t in hs):
            i_p = (1 + round((1 + 24 * t) ** 0.5)) // 6
            i_h = (1 + round((1 + 8 * t) ** 0.5)) // 4
            print('T{} = P{} = H{} = {}'.format(i, i_p, i_h, t))
            amount += 1
        i += 1
    return t


if __name__ == '__main__':
    print('Answer:', problem())
