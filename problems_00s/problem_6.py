"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
"""


def problem(x):
    sum_squares = x * (x + 1) * (2 * x + 1) // 6
    square_sum = (x * (x + 1) // 2) ** 2
    return square_sum - sum_squares

if __name__ == '__main__':
    print('Test:', problem(10))
    print('Answer:', problem(20))
