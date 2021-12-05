import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to the PyPassword Generator")
number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_numbers = int(input("How many numbers would you like? "))

#EASY VERSION TO GENERAGE PASSWORD
password = ""
#assign the password as empty string
for char in range (1,number_of_letters + 1):
    password += random.choice(letters)
    # password = password + random_char
    #string concatentation

for char in range (1,number_of_symbols + 1):
    password += random.choice(symbols)

for char in range (1,number_of_numbers + 1):
    password += random.choice(numbers)

print (password)

# HARD VERSION
# you can only shuffle on lists so need to create password as a list, shuffle and then turn into list with for loop
password_list = []
#assign the password as empty LIST
for char in range (1,number_of_letters + 1):
    password_list.append(random.choice(letters))
    # password = password + random_char
    #+= same thing as append

for char in range (1,number_of_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range (1,number_of_numbers + 1):
    password_list.append(random.choice(numbers))

#change the order of the list with random.shuffle

random.shuffle(password_list)
#creates password in list form however need to revert back to a string through a for function

password = ""
for char in password_list:
    password += char
print (f"Your password is {password}")
