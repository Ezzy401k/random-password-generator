#Password Generator Project
import random
# List the characters that will be needed.
lower_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
upper_letters = [ 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# Ask the user if they want the generator to create the password randomly or if they want custom input.
use = input("If you want a random password type 'y' or for a custom password length type 'n':\n")
# If they want a random password execute this.
if use == "y":
   lr_letters = random.randint(3,7)
   up_letters = random.randint(2,5)
   nr_numbers = random.randint(2,5)
   nr_symbols = random.randint(1,4)
# If the want a custom password run this.
elif use == "n":
    lr_letters = int(input("How many lower case letters would you like in your password?\n"))
    up_letters = int(input("How many upper case letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
# If a wrong input is given.
else:
   print("Please Enter a valid input.")
# Create variables to hold the random characters chosen for the password.
code1 = ''
code2 = ''
code3 = ''
code4 = ''
# Cycle through the characters and choose.
for i in range(0,up_letters):
  temp = random.choice(lower_letters)
  code1 += temp
for i in range(0,lr_letters):
  temp1 = random.choice(upper_letters)
  code2 += temp1
for j in range(0,nr_symbols):
  temp2 = random.choice(symbols)
  code3 += temp2
for k in range(0,nr_numbers):
  temp3 = random.choice(numbers)
  code4 += temp3
# Convert the strings to a list after contacting them.
list_code = list(code1 + code2 + code3+code4)
# shuffle through the list 3 times because I like it.
random.shuffle(list_code)
random.shuffle(list_code)
random.shuffle(list_code)
# Convert the list to a string that gets displayed to the user.
shuffled_passcode = ''
for n in list_code:
  shuffled_passcode += n
print(shuffled_passcode)

input("Tap ENTER to EXIT!")

