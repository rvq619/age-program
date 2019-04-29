age = 5

"I am " + str(age) + " years old"

"I am {} years old".format(age)

"I am {} years and {} months old".format(age, 7)

"I am {age} years old, are you {age} years old too?".format(age=age)

------------------------

input("Enter your age: ")

int(user_age) * 365 * 24 * 60 * 60

seconds = int(user_age) * 365 * 24 * 60 * 60
seconds

print ("you have lived for {} seconds").format(seconds))

--------------------------

def age_in_seconds():
	user_age = input("Enter your age: ")
	age_seconds = int(user_age) * 365 * 24 * 60 * 60
	print("You have lived for {} seconds".format(age_seconds))

age_in_seconds()

--------------------------

def user_name():
	return "Rolf"


def greeting(name):
	return "Hello, {}, how are you?".format(name)
	

--------------------------

price = 100
if price < 100:
	print("Buy chair?")
else:
	print("Don't buy.")


if price < 100:
	print("Buy chair")
elif price == 100:
	print("Buy if you really want.")
else:
	print("Don't buy.")


def age_program():
	seconds_or_years = input("Give me seconds (s) or years (y)?")
	if seconds_or_years == "s":
		# Convert seconds to years
		user_value = input("Enter the number of seconds you've lived for: ")
		print("You've lived for {} years".format(int(user_value) / 60 / 60 / 24 / 365))
	elif seconds_or_years == "y":
		# Convert years to seconds
		user_value = input("Enter the number of years you've lived for: ")
		print("You've lived for {} seconds".format(int(user_value) * 365 * 24 * 60 * 60))
	pass

	age_program()

--------------------------

def user_even():
	number = input("Enter a number: ")
	int_number = int(number)
	if divisible(int_number, 2):
		print("It's even?")
	else:
		print("It's odd...")
	pass

--------------------------

