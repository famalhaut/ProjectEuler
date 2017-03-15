"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
from scipy.special import binom


def problem(a, b):
    return int(round(binom(a + b, b)))


if __name__ == '__main__':
    print('Test:', problem(2, 2))
    print('Answer:', problem(20, 20))
