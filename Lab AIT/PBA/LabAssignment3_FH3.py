# 3. Write Python program to Get number of characters, words, spaces and lines in a file

char_count = 0
word_count = 0
space_count = 0
line_count = 0

with open("questions.txt") as f:
    for line in f:
        line_count += 1


print(char_count)
print(word_count)
print(space_count)
print(line_count)
