def does_key_exists(check_key):
    
    if check_key in positive:
        print(f"\nYes, key = {check_key} is available")
    else:
        print(f"\nNo, key = {check_key} is not available")




def iterate_over_items(negative):
    
    print(f"\nItems in negative dictionary : ")
    for value in negative.items():
        print(value, end = " ")




def dictionary_concat(positive, negative):
    print(f"\n\nInteger dictionary after merging : ")
    global integer
    integer = positive | negative
    print(integer)




def sum_of_values(positive):
    sum = 0
    for value in positive.values():
        sum += value
    print(f"\nSum of values in Positive dictionary: {sum}")




def max_and_min(integer):
    maxi = max(integer.values())
    mini = min(integer.values())
    print(f"\nMaximum value in Integer dictionary = {maxi}")
    print(f"Minimum value in Integer dictionary = {mini}")



positive = {'a': 5, 'b': 10, 'c': 15, 'd': 20, 'e': 25}
negative = {1: -11, 2: -22, 3: -33, 4: -44, 5: -55}
integer = {}
print(f"Dictionaries are :\nPositive = {positive}\nNegative = {negative}")
print(f"Integer = {integer}")

does_key_exists(check_key = 'a')
iterate_over_items(negative)
dictionary_concat(positive, negative)
sum_of_values(positive)
max_and_min(integer)












