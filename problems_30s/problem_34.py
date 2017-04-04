from math import factorial

facts = {}
for i in range(10):
    facts[i] = factorial(i)


def get_max_possible_num():
    order = 1
    while 10 ** order - 1 < order * facts[9]:
        order += 1
    return order * factorial(9)


def problem():
    result = 0

    for num in range(10, get_max_possible_num()):
        s = 0
        temp = num
        while temp > 0:
            s += facts[temp % 10]
            temp //= 10
            if s > num:
                break
        else:
            if num == s:
                print(num, '=', ' + '.join(map(lambda ch: ch + '!', str(num))))
                result += num
    return result


if __name__ == '__main__':
    print('Answer:', problem())
