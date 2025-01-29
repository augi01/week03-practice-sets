# 1. Print its contents line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 2. Count the total number of lines in a file ang display result
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(f'Total number of lines: {len(lines)}')

# 3. Count the number of words in it
with open('example.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print(f'Total number of words: {len(words)}')

# 4. Count the total number of characters
with open('example.txt', 'r') as file:
    content = file.read()
    print(f'Total number of characters: {len(content)}')
