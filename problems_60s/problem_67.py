"""
Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.
---test_nums---
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a
triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route
to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes
every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
"""

test_nums = """3
7 4
2 4 6
8 5 9 3"""
test_data = [list(map(int, row.split())) for row in test_nums.split('\n')]
problem_data = []
with open('p067_triangle.txt', 'r') as f:
    for line in f:
        problem_data.append(list(map(int, line.split())))


def problem(data):
    for row in range(len(data) - 2, -1, -1):
        next_row = data[row + 1]
        for i in range(len(data[row])):
            data[row][i] += max(next_row[i], next_row[i + 1])
    return data[0][0]


if __name__ == '__main__':
    print('Test:', problem(test_data))
    print('Answer:', problem(problem_data))
