def pattern1():
        print("\n\nPattern1\n")
        for row in range(1, 5):                
                for column in range(row):
                        print(column + 1, end = " ")
                print("\n")



def pattern2():
        print("\nPattern2\n")
        for row in range(5, 1, -1):
                for column in range(row - 1):
                        print("*", end = " ")
                print("\n")



                
def pattern3():
        print("\nPattern3\n")
        for row in range(5, 0, -1):
                for column in range(row):
                        print(row, end = " ")
                print("\n")



                
def pattern4():
        print("\nPattern4\n")
        letter = 65
        for row in range(1, 6):                
                for column in range(row):
                        print(chr(letter), end = " ")
                        letter += 1
                print("\n")



                
pattern1()
pattern2()
pattern3()
pattern4()
