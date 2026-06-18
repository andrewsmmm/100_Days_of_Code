'''100 Days of Code: Password Generator Project '''
# note: this is my second attempt at this project after seeing Angela's solution.
# I used a while loop when I needed to use a for in range loop
# I figured out the append and random.choice parts adding to the new password_list list.
# I kept the random shuffle action and the "".join() method to print the password
# as a string instead of a list.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Code block for pulling the required number of letters, number and symbols
password_list = []
for character in range(0, nr_letters):
    password_list.append(random.choice(letters))

for character in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for character in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(("Here is your password: ") + "".join(password_list))
