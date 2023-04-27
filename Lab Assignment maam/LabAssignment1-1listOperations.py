def sum_list_items(numbers):
    print("sum = ", sum(numbers))



def max_list_items(numbers):
    print("Largest number = ", max(numbers))



def remove_duplicates(numbers):
    for no in numbers:
        if numbers.count(no) > 1:
            while numbers.count(no) > 1:
                numbers.remove(no)
    print(f"Duplicates removed : {numbers}")



def separate_pos_neg(numbers):
    positive, negative = [], []
    for no in numbers:
        if no > 0:
            positive.append(no)
        else:
            negative.append(no)
    print(f"Positive nos = {positive} and Negative nos = {negative}")



def filter_even_odd(numbers):
    even, odd = [], []
    for no in numbers:
        if no % 2 == 0:
            even.append(no)
        else:
            odd.append(no)
    print(f"Even nos = {even} and Odd nos = {odd}")


    
numbers = [5, 10, 10, -15, 5, 20, 25]
print(f"List of numbers = {numbers}\n")

sum_list_items(numbers)
max_list_items(numbers)
remove_duplicates(numbers)
separate_pos_neg(numbers)
filter_even_odd(numbers)
