"""
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def sum_divisors(x):
    sum_divs = 0
    for div in range(1, x // 2 + 1):
        if x % div == 0:
            sum_divs += div
    return sum_divs


def problem(x):
    result = 0
    for a in range(3, x):
        b = sum_divisors(a)
        temp = sum_divisors(b)
        if a == temp and a != b:
            result += a
    return result

if __name__ == '__main__':
    print('Answer:', problem(10000))
