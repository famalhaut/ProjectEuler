"""
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in
general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


def problem(r, coin):
    result = 0
    for i in range(r // coin + 1):
        if d[coin] == 1:
            result += 1
        else:
            new_r = r - i * coin
            if new_r == 0:
                result += 1
            else:
                result += problem(new_r, d[coin])
    return result


if __name__ == '__main__':
    d = {200: 100, 100: 50, 50: 20, 20: 10, 10: 5, 5: 2, 2: 1}
    print('Answer:', problem(200, 200))
