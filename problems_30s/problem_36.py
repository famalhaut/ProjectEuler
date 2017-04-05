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
