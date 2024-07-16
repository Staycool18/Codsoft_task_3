import random
import string

password_length=int(input("Enter Length of password"))

elements=string.ascii_letters
elements+=string.digits
elements+=string.punctuation

password=""

for i in range(password_length):
    next_character=random.choice(elements)
    password+=next_character
    
print("Random Password Generated is:",password)