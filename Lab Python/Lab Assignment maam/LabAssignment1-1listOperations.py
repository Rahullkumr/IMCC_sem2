numbers = [5, 10, 10, -15, 5, 20, 25]
print(f"List of numbers = {numbers}\n")



# sum of list items
print("sum = ", sum(numbers))



# Maximum of list items
print("Largest number = ", max(numbers))



# remove duplicates from list
for no in numbers:
        if numbers.count(no) > 1:
                while numbers.count(no) > 1:
                        numbers.remove(no)
print(f"Duplicates removed : {numbers}")



# separate positive and negative elements
positive, negative = [], []
for no in numbers:
        if no > 0:
                positive.append(no)
        else:
                negative.append(no)
print(f"Positive nos = {positive} and Negative nos = {negative}")



# filter even and odd numbers
even, odd = [], []
for no in numbers:
        if no % 2 == 0:
                even.append(no)
        else:
                odd.append(no)
print(f"Even nos = {even} and Odd nos = {odd}")

