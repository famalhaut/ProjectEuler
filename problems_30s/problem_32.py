from itertools import permutations


def get_num(permut, ln, shift):
    num = 0
    for i in range(shift, shift + ln):
        num *= 10
        num += permut[i]
    return num


result = set()
for permut in permutations(range(1, 10)):
    # 1-digit * 4-digit = 4-digit
    a = get_num(permut, 1, 0)
    b = get_num(permut, 4, 1)
    c = get_num(permut, 4, 5)
    if a * b == c:
        result.add(c)

    # 2-digit * 3-digit = 4-digit
    a = get_num(permut, 2, 0)
    b = get_num(permut, 3, 2)
    c = get_num(permut, 4, 5)
    if a * b == c:
        result.add(c)

print(result)
print(sum(result))
