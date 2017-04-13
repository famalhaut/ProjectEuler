"""
Sub-string divisibility
Problem 43 
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 
to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""


def problem():
    result = 0
    digits = set(map(str, range(0, 10)))
    for d8_d9_d10 in range(17, 1000, 17):
        for d5_d6_d7 in range(14, 1000, 7):
            d6_d7_d8 = (d5_d6_d7 % 100) * 10 + d8_d9_d10 // 100
            d7_d8_d9 = (d5_d6_d7 % 10) * 100 + d8_d9_d10 // 10
            if d6_d7_d8 % 11 == 0 and d7_d8_d9 % 13 == 0:
                for d2_d3_d4 in range(2, 1000, 2):
                    d3_d4_d5 = (d2_d3_d4 % 100) * 10 + d5_d6_d7 // 100
                    d4_d5_d6 = (d2_d3_d4 % 10) * 100 + d5_d6_d7 // 10
                    if d3_d4_d5 % 3 == 0 and d4_d5_d6 % 5 == 0:
                        nums = [d2_d3_d4, d5_d6_d7, d8_d9_d10]
                        current_digits = ''.join(map(lambda x: str(x).zfill(3), nums))

                        if len(set(current_digits)) == 9:
                            d1 = (digits - set(current_digits)).pop()
                            res = int(d1 + current_digits)
                            print(res)
                            result += res
    return result


if __name__ == '__main__':
    print('Answer:', problem())
