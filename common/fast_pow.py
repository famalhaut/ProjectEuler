def problem(x):
    tmp = 1
    for i in map(int, bin(x)[2:]):
        tmp **= 2
        tmp *= 2 ** i
    return tmp