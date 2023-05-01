print("\n\nPattern1\n")
for row in range(1, 5):
        for column in range(row):
                print(column + 1, end = " ")
        print("\n")

print("\nPattern2\n")
for row in range(5, 1, -1):
        for column in range(row - 1):
                print("*", end = " ")
        print("\n")

print("\nPattern3\n")
for row in range(5, 0, -1):
        for column in range(row):
                print(row, end = " ")
        print("\n")

print("\nPattern4\n")
letter = 65
for row in range(1, 6):
        for column in range(row):
                print(chr(letter), end = " ")
                letter += 1
        print("\n")
