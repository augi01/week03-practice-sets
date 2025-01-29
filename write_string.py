strings = ["macbook", "iphone", "samsung", "itel", "infinix", "vivo"]
with open('strings.txt', 'w') as file:
    for string in strings:
        file.write(string + "\n")
