with open('p042_words.txt') as f:
    words_string = f.read()

words = map(lambda word: word.replace('"', ''), words_string.split(','))

result = 0
triangle_nums = [n * (n + 1) // 2 for n in range(1, 30)]

# words = ['SKY']
for word in words:
    word_value = sum(map(lambda ch: ord(ch) - ord('A') + 1, word))
    if word_value in triangle_nums:
        result += 1

print(result)