"""
Integer right triangles
Problem 39 
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are 
exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def gcd(x, y):
    if x <= y:
        x, y = y, x

    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def problem(lim):
    counter = {}
    for n in range(1, int(lim ** 0.5) + 1):
        for m in range(n + 1, int(lim ** 0.5) + 1):
            if ((m - n) % 2 == 1) and gcd(m, n) == 1:
                p = 2 * m * (m + n)
                perimeter = p
                while perimeter <= lim:
                    if perimeter in counter:
                        counter[perimeter] += 1
                    else:
                        counter[perimeter] = 1
                    perimeter += p

    return max(counter.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    print('Answer:', problem(1000))
