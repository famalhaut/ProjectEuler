"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_seq(d, less_than):
    """
    S =  d + 2d + 3d + ... + nd
    dn < less_than
    """
    n = (less_than - 1) // d
    return d * n * (n + 1) / 2


def problem(less_than):
    sum_div_3 = sum_seq(3, less_than)
    sum_div_5 = sum_seq(5, less_than)
    sum_div_15 = sum_seq(15, less_than)
    return int(sum_div_3 + sum_div_5 - sum_div_15)

if __name__ == '__main__':
    print('Test:', problem(10))
    print('Answer:', problem(1000))
