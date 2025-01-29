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

