# Firstly import random and string
# The module secrets works very similarly to the way of the module random
import secrets
import string
# Print this is a password generator
print('This is a Password Generator')

# Password customization
print(
    '1. Password should contain alphabets, numbers and symbols'
    '\n2. Password should not contain symbols '
    '\n3. Password should not contain alphabets '
    '\n4. Password should not contain numbers '
    '\n5. Password should not contain both alphabets and numbers '
    '\n6. Password should not contain both numbers and symbols '
    '\n7. Password should not contain both alphabets and symbols'
)

# Ask user which option they prefer1
option = input('What option do you prefer: ')

# Ask user how many characters the generated password should have
password_length = input('How many characters should the generated password have: ')
# print(type(int(password_length)))
# The characters password is generated from

alphabets_values = string.ascii_letters
numbers_values = string.digits
symbols_values = string.punctuation

characters_alphabets = alphabets_values
characters_numbers = numbers_values
characters_symbols = symbols_values
characters_all = alphabets_values + numbers_values + symbols_values
characters_alphabet_numbers = alphabets_values + numbers_values
characters_alphabet_symbols = alphabets_values + symbols_values
characters_numbers_symbols = numbers_values + symbols_values


password = ''

if option == '1':
    for i in range(int(password_length)):
        password += ''.join(secrets.choice(characters_all))
    print('Your generated password is -----  ' + password)
elif option == '2':
    for i in range(int(password_length)):
        password += ''.join(secrets.choice(characters_alphabet_numbers))
    print('Your generated password is -----  ' + password)
elif option == '3':
    for i in range(int(password_length)):
        password += ''.join(secrets.choice(characters_numbers_symbols))
    print('Your generated password is -----  ' + password)
elif option == '4':
    for i in range(int(password_length)):
        password += ''.join(secrets.choice(characters_alphabet_symbols))
    print('Your generated password is -----  ' + password)
elif option == '5':
    for i in range(int(password_length)):
        password += ''.join(secrets.choice(characters_symbols))
    print('Your generated password is -----  ' + password)
elif option == '6':
    for i in range(int(password_length)):
        password += ''.join(secrets.choice(characters_alphabets))
    print('Your generated password is -----  ' + password)
elif option == '7':
    for i in range(int(password_length)):
        password += ''.join(secrets.choice(characters_numbers))
# if password_length or option == alphabets_values or symbols_values:
#     print('You have made an error in filling in how many characters should be in the password')
