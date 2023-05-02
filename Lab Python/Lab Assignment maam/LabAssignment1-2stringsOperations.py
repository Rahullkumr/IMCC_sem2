str = "Python Lab Ass!gnment1"
print(f"Original String : {str}")



# Reverse the string
print("\nReversed string : ")
print(str[::-1])



# change each lower case letter to upper and vice-versa 
# In python, swapcase() can do it in just one line ⬇
# print(str.swapcase())
nos = "0123456789"
print("\nSwapping case of letters in String: ")
for letter in str:
    if letter in nos:
        print(letter, end= "")
    elif letter.isupper():
        print(letter.lower(), end= "")
    else:
        print(letter.upper(), end= "")



# count vowels, consonants, letters, lower case, upper case, 
# numbers and special characters
vowel = "aeiouAEIOU"
consont = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
v_count = 0
c_count = 0
lower_count = 0
upper_count = 0
no_count = 0
spcl_char_count = 0

for letter in str:
        if letter in vowel:         
            v_count += 1
        elif letter in consont:
            c_count += 1
        elif letter in nos:
            no_count += 1
        else:
            spcl_char_count += 1

        if letter.isupper():
            upper_count += 1

        if letter.islower():
            lower_count += 1

print(f"\n\nTotal vowels = {v_count} \nTotal consonants = {c_count}")
print(f"\nTotal Letters : {v_count + c_count}")
print("\nTotal lower case: ",lower_count)
print("Total upper case: ",upper_count)
print("Total numbers: ",no_count)
print("Total special chars: ",spcl_char_count)
