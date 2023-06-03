# 3. Write Python program to Get number of characters, words, spaces and lines in a file

char_count, word_count, space_count, line_count = 0, 0, 0, 0

with open("questions.txt") as f:
    content = f.read()
    char_count = len(content)
    word_count = content.split()
    space_count = content.count(' ')
    line_count = content.count('\n') + 1
    
    print(char_count)
    print(word_count)
    print(space_count)
    print(line_count)
