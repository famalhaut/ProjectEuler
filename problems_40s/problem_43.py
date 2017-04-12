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

result = 0
for digits_3 in range(17, 1000, 17):
    for digits_2 in range(7, 1000, 7):
        d6d7d8 = (digits_2 % 100) * 10 + digits_3 // 100
        d7d8d9 = (digits_2 % 10) * 100 + digits_3 // 10
        if d6d7d8 % 11 == 0 and d7d8d9 % 13 == 0:
            for digits_1 in range(2, 1000, 2):
                d3d4d5 = (digits_1 % 100) * 10 + digits_2 // 100
                d4d5d6 = (digits_1 % 10) * 100 + digits_2 // 10
                if d3d4d5 % 3 == 0 and d4d5d6 % 5 == 0:
                    digits = set.union(*map(lambda x: set(str(x)), [digits_1, digits_2, digits_3]))
                    if len(digits) == 8 and (10 <= digits_1 <= 99) and ('0' not in digits):
                        for digit in set(map(str, range(0, 10))) - digits - {'0'}:
                            res = int(digit + '0' + str(digits_1) + str(digits_2) + str(digits_3))
                            print(res)
                            result += res
                    elif len(digits) == 9 and ('0' in digits) and (100 <= digits_1):
                        for digit in set(map(str, range(0, 10))) - digits:
                            res = int(digit + str(digits_1) + str(digits_2) + str(digits_3))
                            print(res)
                            result += res

print('ans', result)