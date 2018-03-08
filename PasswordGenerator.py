# Password Generator

def user_pass_length():
	validtype = False
	validlength = False
	while validtype == False:	# evaluates whether the user input is an integer
		try:
			pass_length = int(input("How long would you like your password to be?(<17)"))
			validtype = True
		except ValueError:
			print("I'm sorry that is not an integer, please try again")	
	for x in range(1, 16):	# evaluates user input password length
		if x == pass_length:
			print("That is a GOOD number")
			validlength = True
			break
		else:
			validlength = False	
	if validtype and validlength:	# evaluates both booleans for a final decision
		print("Completed.")
	else:
		print("I'm sorry but that is not a valid password length, please try again")
		user_pass_length()

	placeholder = input("Press again to exit")











user_pass_length()


alpha_up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alpha_down = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
integer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
spec_list = ["?", "!", "&", "$", "#"]
