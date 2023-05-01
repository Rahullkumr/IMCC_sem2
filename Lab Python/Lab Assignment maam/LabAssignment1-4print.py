# print first ten natural numbers
print("\nFirst ten Natural numbers")
for nos in range(1,11):
        print(nos, end = " ")




# print first ten even numbers
print("\n\nTen Even numbers in reverse")
for nos in range(20, 1, -2):
        print(nos, end = " ")




# print table of given number
num = int(input("\n\nEnter number to get table: "))
for i in range(1,11):
        print(num * i)




# print first ten prime numbers
def is_prime(num):
    true_or_false = True
    
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            true_or_false = False
    return true_or_false

print("\nFirst ten Prime numbers")
for no in range(2, 30):
        if is_prime(no):
                print(no, end = " ")

