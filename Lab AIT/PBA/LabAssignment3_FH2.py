# 2. Write Python program to read character by character from a file

with open("file1.txt") as f:

    while True:
        char = f.read(1)
        print(char)
        if char == '':
            break
