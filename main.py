import random
import string
num_of_chars_str = ''
while type(num_of_chars_str) != int:
    num_of_chars_str = input("Please enter the amount of characters you want to have in your password: ")
    try:
        num_of_chars = int(num_of_chars_str)
    except ValueError:
        print("You did not type in an integer. Please try again")
num_of_chars = int(num_of_chars)


password = ""
for i in range(num_of_chars):
    i = random.choice(string.ascii_letters)
    password += i

print(password)

