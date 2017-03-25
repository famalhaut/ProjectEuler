"""
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is
formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def problem(x):
    result = 1
    for len_square in range(3, x + 1, 2):
        result += 4 * len_square ** 2 - 6 * (len_square - 1)
    return result


if __name__ == '__main__':
    print('Test:', problem(5))
    print('Answer:', problem(1001))
