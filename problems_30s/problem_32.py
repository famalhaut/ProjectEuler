"""
Pandigital products
Problem 32 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly 
once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written 
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once 
in your sum.
"""


def problem():
    result = set()

    def _helper(a, b):
        c = a * b
        digits = set(str(a)) | set(str(b)) | set(str(c))
        if len(digits - {'0'}) == 9:
            print('{a} * {b} = {c}'.format(a=a, b=b, c=c))
            result.add(c)

    # 1-digit * 4-digit = 4-digit
    for a in range(1, 10):
        for b in range(1000, 10000 // a):
            _helper(a, b)

    # 2-digit * 3-digit = 4-digit
    for a in range(10, 100):
        for b in range(100, 10000 // a):
            _helper(a, b)

    return sum(result)


if __name__ == '__main__':
    print('Answer:', problem())
