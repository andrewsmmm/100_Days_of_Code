'''100 Days of Code: Password Generator Project '''

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

# I couldn't figure out how to pull multiple letters etc. from the list, so I used the while loop to
# pull the letters, numbers and symbols from the list. I also tried using random.shuffle() but it didn't work for me.

# Code block for pulling the required number of letters
letters_list = []
while len(letters_list) != nr_letters:
    letters_list.append(random.choice(letters))


# Code block for pulling the required number of numbers
numbers_list = []
while len(numbers_list) != nr_numbers:
    numbers_list.append(random.choice(numbers))

# Code block for pulling the required number of symbols
symbols_list = []
while len(symbols_list) != nr_symbols:
    symbols_list.append(random.choice(symbols))

# Code block for combining the chosen letters, numbers and symbols
# Couldn't figure out how to combine and randomize them with assigning a new variable
# I found that I had to use join again on the password variable as without it it just printed password as a list
password = letters_list + numbers_list + symbols_list
random.shuffle(password)
print(("Here is your password: ") + "".join(password))