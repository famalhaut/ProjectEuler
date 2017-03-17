"""
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
five-thousand first names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

with open('p022_names.txt', 'r') as f:
    names_list = list(map(lambda x: x[1:-1].upper(), f.read().split(',')))


def problem(names):
    names.sort()
    result = 0
    for i, name in enumerate(names):
        result += (i + 1) * sum(map(lambda ch: ord(ch) - 64, name))
    return result


if __name__ == '__main__':
    print('Answer:', problem(names_list))
