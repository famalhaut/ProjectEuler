"""
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers
of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def get_max_possible_num(pw):
    order = 2
    while 10 ** order <= order * (9 ** pw):
        order += 1
    return order * (9 ** pw) + 1


def problem(pw):
    result = []
    for num in range(10, get_max_possible_num(pw)):
        temp = num
        total = 0
        while temp != 0 and total <= num:
            total += (temp % 10) ** pw
            temp //= 10
        if total == num:
            result.append(num)
    return result


if __name__ == '__main__':
    answer_4 = problem(4)
    answer_5 = problem(5)
    print('Test: {sum} {nums}'.format(sum=sum(answer_4), nums=answer_4))
    print('Answer: {sum} {nums}'.format(sum=sum(answer_5), nums=answer_5))
