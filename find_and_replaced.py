word_to_replace = "old"
replacement_word = "new"
with open('file.txt', 'r') as file:
    content = file.read()

content = content.replace(word_to_replace, replacement_word)

with open('file.txt', 'w') as file:
    file.write(content)

