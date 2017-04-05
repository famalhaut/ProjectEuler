from common.primes import miller_rabin_test


def problem(lim):
    circular_primes = list(filter(lambda x: x < lim, [2, 3, 5]))
    for num in range(7, lim, 2):
        temp = num
        digits = []
        while temp > 0:
            digits.append(temp % 10)
            temp //= 10

        if not ({0, 2, 4, 6, 8, 5} & set(digits)):
            for _ in range(len(digits)):
                rotation = 0
                for i in digits:
                    rotation *= 10
                    rotation += i
                if miller_rabin_test(rotation):
                    digits = digits[1:] + digits[:1]
                else:
                    break
            else:
                circular_primes.append(num)
    return circular_primes


if __name__ == '__main__':
    print('Answer:', len(problem(10**6)))
