def ten_natural_nos():
    print("\nFirst ten Natural numbers")
    for nos in range(1,11):
        print(nos, end = " ")




def ten_even_nos():
    print("\n\nTen Even numbers in reverse")
    for nos in range(20, 1, -2):
        print(nos, end = " ")




def table_of_no():
    num = int(input("\n\nEnter number to get table: "))
    for i in range(1,11):
        print(num * i)



              
def is_prime(num):
    true_or_false = True
    
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            true_or_false = False
    return true_or_false

def ten_prime_nos():
    print("\nFirst ten Prime numbers")
    for no in range(2, 30):
        if is_prime(no):
            print(no, end = " ")



            
ten_natural_nos()
ten_even_nos()
table_of_no()
ten_prime_nos()
