# Password Generator

import secrets



def user_pass_length():
	validtype = False
	validlength = False
	while validtype == False:	# evaluates whether the user input is an integer
		try:
			pass_length = int(input("How long would you like your password to be?(<17)\n"))
			validtype = True
		except ValueError:
			print("I'm sorry that is not an integer, please try again")	
	for x in range(1, 17):	# evaluates user input password length
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
	return pass_length
	placeholder = input("Press again to exit")

def user_upcase():
	validans = True
	while validans:		
		upcase = input("Would you like your password to have uppercase letters?(y/n)\n")
		if upcase.lower() == "y":
			upcase_final = True
			validans = False
		elif upcase.lower() == "n":
			upcase_final = False
			validans = False
		else:
			print("Sorry that is not a valid answer, please try again.")
			validans = True
	return upcase_final

def user_integer():
	validans = True
	while validans:		
		raw = input("Would you like your password to have numbers?(y/n)\n")
		if raw.lower() == "y":
			integer_final = True
			validans = False
		elif raw.lower() == "n":
			integer_final = False
			validans = False
		else:
			print("Sorry that is not a valid answer, please try again.")
			validans = True
	return integer_final

def user_spec():
	validans = True
	while validans:		
		raw = input("Would you like your password to have special characters?(y/n)\n")
		if raw.lower() == "y":
			spec_final = True
			validans = False
		elif raw.lower() == "n":
			spec_final = False
			validans = False
		else:
			print("Sorry that is not a valid answer, please try again.")
			validans = True
	return spec_final


alpha_up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alpha_down = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
integer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
spec_list = ["?", "!", "&", "$", "#"]

# random number - index the list
# random number 1 - 4 to reference each list through indexing a list with those lists inside of it 

def main():
	char_list = [alpha_up, alpha_down, integer_list, spec_list]
	if upcase_final and integer_final and spec_final:
		print("Your final password is: \n")
	for i in range(0, pass_length):
		temp = char_list[secrets.randbelow(4)]
		temp = temp[secrets.randbelow(len(temp))]
		print(temp, end="")
	placeholder = input("\nplaceholder")


pass_length = user_pass_length()
upcase_final = user_upcase()
integer_final = user_integer()
spec_final = user_spec()
print(pass_length, " ", upcase_final, " ", integer_final, " ", spec_final)
main()
print("\nThank you for using Connor's password generator!")

