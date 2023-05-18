# 1. Write Python program to read file word by word

with open("file1.txt") as f:
    content = f.read()
    word_list = content.split()

    for word in word_list:
        print(word)
