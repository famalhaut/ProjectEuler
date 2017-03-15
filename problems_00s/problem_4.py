"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def problem(x):
    palindromics = []
    for i in range(10 ** (x - 1), 10 ** x):
        for j in range(i, 10 ** x):
            if i * j == int(str(i * j)[::-1]):
                palindromics.append(i * j)
    return max(palindromics)


if __name__ == '__main__':
    print('Test:', problem(2))
    print('Answer:', problem(3))
