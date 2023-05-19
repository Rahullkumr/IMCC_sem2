# Write Python program to Append content of one text file to another

with open("file1.txt") as file1:
    f1_content = file1.read()

with open("file2.txt", "a") as file2:
    file2.write(f1_content)
