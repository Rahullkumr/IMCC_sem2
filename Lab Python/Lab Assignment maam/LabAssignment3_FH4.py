# Write Python program to Count the Number of occurrences of a key-value pair in a text file

with open("file1.txt") as file:
    count = 0
    key, value = 'Name', 'Rahul'
    
    for line in file:
      if key in line and value in line:
        count += 1
print(count)
