# 1. Write "Hello, World!" into it
with open('source.txt', 'w') as file:
    file.write("Hello, World!\n")

# 2. Append text to an existing file
with open('source.txt', 'a') as file:
    file.write("This is appended text to an existing file.")

# 3. Copy contents from source.txt to destination.txt
with open('source.txt', 'r') as src_file:
    content = src_file.read()

with open('destination.txt', 'w') as dest_file:
    dest_file.write(content)

# 4. Write a list of strings to it, each string into a new line
strings = ["apple", "banana", "cherry"]
with open('strings.txt', 'w') as file:
    for string in strings:
        file.write(string + "\n")

# 5. Write numbers from 1 to 10 to a file, each on a new line
with open('numbers.txt', 'w') as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")
