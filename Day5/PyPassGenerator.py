import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


print("Welcome to the PyPassword Generator!")
rp_letters = int(input("How many letters would you like in your password? > "))
rp_numbers = int(input("How many numbers would you like in your password? > "))
rp_symbols = int(input("How many symbols would you like in your password? > "))

password = ""
password_place_holder = []

# Random Letters
for char in range(1, rp_letters + 1):
    random_char = random.choice(letters)
    password_place_holder.append(random_char)

# Random Numbers
for number in range(1, rp_numbers + 1):
    random_num = random.choice(numbers)
    password_place_holder.append(random_num)

# Random Symbols
for symbol in range(1, rp_symbols + 1):
    random_sym = random.choice(symbols)
    password_place_holder.append(random_sym)

random.shuffle(password_place_holder)

password = ""
for char in password_place_holder:
    password += char

print(f"Your random generated password is: {password}")
