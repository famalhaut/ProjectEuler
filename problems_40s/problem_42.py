"""
Coded triangle numbers
Problem 42 
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten 
triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and 
adding these values we form a word value. For example, the word value for SKY is 
19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word 
a triangle word.

Using p042_words.txt , a 16K text file containing nearly two-thousand common English words, 
how many are triangle words?
"""


def problem():
    with open('p042_words.txt') as f:
        words_string = f.read()

    words = list(map(lambda word: word.replace('"', ''), words_string.split(',')))

    n = 1
    triangle_num = 1
    triangle_nums = set()
    max_len = len(max(words, key=len))
    while triangle_num <= 26 * max_len:
        triangle_num = n * (n + 1) // 2
        triangle_nums.add(triangle_num)
        n += 1

    result = 0
    for word in words:
        word_value = sum(map(lambda ch: ord(ch) - ord('A') + 1, word))
        if word_value in triangle_nums:
            result += 1

    return result


if __name__ == '__main__':
    print('Answer:', problem())
