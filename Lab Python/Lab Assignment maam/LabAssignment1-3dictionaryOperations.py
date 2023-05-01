positive = {'a': 5, 'b': 10, 'c': 15, 'd': 20, 'e': 25}
negative = {1: -11, 2: -22, 3: -33, 4: -44, 5: -55}
integer = {}
print(f"Dictionaries are :\nPositive = {positive}\nNegative = {negative}")
print(f"Integer = {integer}")




# check whether key = 'a' exists or not
check_key = 'a'
if check_key in positive:
        print(f"\nYes, key = {check_key} is available")
else:
        print(f"\nNo, key = {check_key} is not available")




# iterate over items
print(f"\nItems in negative dictionary : ")
for value in negative.items():
        print(value, end = " ")




# dictionary concatenation or merging two dictionaries
print(f"\n\nInteger dictionary after merging : ")
integer = positive | negative
print(integer)




# sum of values
sum = 0
for value in positive.values():
        sum += value
print(f"\nSum of values in Positive dictionary: {sum}")




# maximum and minimum value from Integer dictionary
maxi = max(integer.values())
mini = min(integer.values())
print(f"\nMaximum value in Integer dictionary = {maxi}")
print(f"Minimum value in Integer dictionary = {mini}")
