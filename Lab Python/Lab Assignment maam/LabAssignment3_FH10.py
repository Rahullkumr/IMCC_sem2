# Write Python program to merge two files into a third file

with open("file1.txt") as file1:
    f1_content = file1.read()

with open("file2.txt") as file2:
    f2_content = file2.read()

with open("mergedFile.txt", "x") as file3:
    file3.write(f1_content)
    file3.write("\n")
    file3.write(f2_content)
