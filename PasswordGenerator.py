# Password Generator

import secrets

alpha_up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alpha_down = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
integer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
spec_list = ["?", "!", "&", "$", "#"]

def user_pass_length():
  invalidans = True
  while invalidans:
    validtype = False
    validlength = False
    while validtype == False:       # evaluates whether the user input is an integer
      try:
        pass_length = int(input("How long would you like your password to be?(<17)\n"))
        validtype = True
      except ValueError:
        print("I'm sorry, that is not an integer, please try again")  
    for x in range(1, 17):          # evaluates user input password length
      if x == pass_length:
        validlength = True
        break
      else:
        validlength = False 
    if validtype and validlength:   # evaluates both booleans for a final decision
      invalidans = False
    else:
      print("I'm sorry but that is not a valid password length, please try again")
      invalidans = True
  return pass_length

def user_upcase():
  invalidans = True
  while invalidans:   
    upcase = input("Would you like your password to have uppercase letters?(y/n)\n")
    if upcase.lower() == "y":
      invalidans = False
      upcase_final = True
    elif upcase.lower() == "n":
      invalidans = False
      upcase_final = False
    else:
      print("Sorry that is not a valid answer, please try again.")
      invalidans = True
  return upcase_final

def user_integer():
  invalidans = True
  while invalidans:   
    raw = input("Would you like your password to have numbers?(y/n)\n")
    if raw.lower() == "y":
      invalidans = False
      integer_final = True
    elif raw.lower() == "n":
      invalidans = False
      integer_final = False
    else:
      print("Sorry that is not a valid answer, please try again.")
      invalidans = True
  return integer_final

def user_spec():
  invalidans = True
  while invalidans:   
    raw = input("Would you like your password to have special characters?(y/n)\n")
    if raw.lower() == "y":
      invalidans = False
      spec_final = True
    elif raw.lower() == "n":
      invalidans = False
      spec_final = False
    else:
      print("Sorry that is not a valid answer. Please try again.")
      invalidans = True
  return spec_final

def main():
  print("Your final password is:")
  for i in range(0, pass_length):
    temp = char_list[secrets.randbelow(len(char_list))]   # indexing char_list for one of the above 4 lists
    temp = temp[secrets.randbelow(len(temp))]             # generating random number below the length of the list just chosen and indexes it
    print(temp, end="")

pass_length = user_pass_length()
char_list = [alpha_down]

if user_upcase():
  char_list.append(alpha_up)

if user_integer():
  char_list.append(integer_list)

if user_spec():
  char_list.append(spec_list)

main()
print("\n\nThank you for using Connor's password generator!")