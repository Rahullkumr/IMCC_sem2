# 6. Write Python program to Count number of lines in a text file in Python

line_count = 0

with open("questions.txt") as f:
    for lines in f:
        line_count += 1
print(line_count)

# Other way for above program
#     while True:
#         print(f.readline())
#         if not f.readline():
#             break
