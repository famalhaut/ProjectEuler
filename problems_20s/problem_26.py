"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a
6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
"""


def problem(x):
    result = 0
    max_cycle = 0
    for d in range(2, x):
        remainder = 1
        rs = dict()
        idx = 1
        while True:
            remainder = remainder % d
            remainder *= 10

            if remainder not in rs:
                rs[remainder] = idx
                idx += 1
            else:
                cycle_len = idx - rs[remainder]
                if max_cycle < cycle_len:
                    max_cycle = cycle_len
                    result = d
                break
    return result


if __name__ == '__main__':
    print('Test:', problem(11))
    print('Answer:', problem(1000))
