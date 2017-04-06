"""
Double-base palindromes
Problem 36 
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def problem():
    db_palindromes = []

    for num in range(1, 10):
        binary = bin(num)[2:]
        if binary == binary[::-1]:
            db_palindromes.append(num)

    for num in range(1, 1000):
        probable = int(str(num) + str(num)[::-1])
        binary = bin(probable)[2:]
        if binary == binary[::-1]:
            db_palindromes.append(probable)

    for num in range(1, 100):
        for center in range(10):
            probable = int(str(num) + str(center) + str(num)[::-1])
            binary = bin(probable)[2:]
            if binary == binary[::-1]:
                db_palindromes.append(probable)
    return db_palindromes


if __name__ == '__main__':
    print('Answer:', sum(problem()))
