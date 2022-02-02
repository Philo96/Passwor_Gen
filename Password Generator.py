
                                            # DO NOT USE MY CODE FOR COMMERCIAL PURPOSES

# importing random:

import random

# The Letters List:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', '\''
                        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', '\''
                        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# The Numbers List:

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# The Symbols List:

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# The Start Of Program:

print("Welcome to the PyPassword Generator!")

# User Inputs:

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# The Main Lines Of Program:
# Letters:

x = []
for letter in range(1, nr_letters+1):
    x.append(random.choice(letters))

# Symbols:

y = []
for symbol in range(1, nr_symbols+1):
    y.append(random.choice(symbols))

# Numbers:

z = []
for number in range(1, nr_numbers+1):
    z.append(random.choice(numbers))

# Generate A Password:

password = (x+y+z)

# Randomisation Of Password:

random.shuffle(password)

# Finally, Make It HArd To crack:

password_x = ""
for char in password:
    password_x += char

# Then Printing It:

print(f"Your Password IS:\n{password_x}")

'''
IMPORTANT NOTES:
1_ You Can Make The Most Strongest Password In The World
2_ This Is The Most Simple App To Make It For U For Free
3_ To Make The Most Strongest Password In The World Follow This Instructions:
    1. Make It TEN Letters.
    2. Make It SIX Symbols.
    3. Make It FOUR Numbers. 
'''