def age_program():
	# ask user for input
	user_age = input("Enter your age: ")
	# convert input to integer and compute seconds
	age_seconds = int(user_age) * 365 * 24 * 60 * 60
	# print to screen results
	print("Your age in seconds is {}".format(age_seconds))
	pass

age_program()