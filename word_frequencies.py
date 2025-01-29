from collections import Counter
with open('file.txt', 'r') as file:
    content = file.read().split()

word_count = Counter(content)

with open('word_frequencies.txt', 'w') as file:
    for word, count in word_count.items():
        file.write(f'{word}: {count}\n')
