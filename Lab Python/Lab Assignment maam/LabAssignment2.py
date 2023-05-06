# 1. Write a program to demonstrate Nested function 

# def nestedfn(num):
# 	def is_even(num):
# 		if num % 2 == 0:
# 			return True
# 		else:
# 			return False

# 	if is_even(num):
# 		print(f"{num} is an EVEN number")
# 	else:
# 		print(f"{num} is an ODD number")

		
# num = int(input("\nEnter an integer: "))
# nestedfn(num)




# 2. Write a program to calculate factorial of a given number using recursion
# def facto(n):
# 	if n == 0:
# 		return 1
# 	return n * facto(n - 1)

# n = int(input("\nEnter an integer: "))
# print(f"Factorial of {n} is {facto(n)}")




# 3. Write a program to create decorators and generators
def decorator_fn(fn_name):
	def double_it(no):
		fn_name(no * 2)
	return double_it

@decorator_fn
def display(no):
	print(no)

def generator_fn():
	for i in range(1, 11):
		yield (i)

print("Combination of generator fn and decorator fn")
print("Generator -> generating 1 to 10")
print("Decorator -> doubling Generator, then printing \n")
numbers = generator_fn()
for no in numbers:
	display(no)


	

# 4. Create two different user defined modules and access respective functions from one file to another
# import user_module2 as um2

# name = input("\nEnter your name: ")
# um2.assign_roll(name)




# 5. write a program to access built-in functions available in math, random and datetime modules
# import math
# import random
# import datetime as dt

# now = dt.datetime.now()
# print(f"\nToday's Date and time : {now}")
# print(f"Year : {now.year}")
# print("Month : ", now.strftime("%B"))
# print("Day : ", now.strftime("%A"))


# rand = random.uniform(1, 10)
# print(f"\nRandom number generated = {rand}")

# print(f"\nFloor value of random number: {math.floor(rand)}")
# print(f"Ceil value of random number: {math.ceil(rand)}")
