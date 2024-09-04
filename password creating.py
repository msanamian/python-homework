from random import *

def generate_password(lenght, chars):
    list_of_symbols_for_password = sample(chars, lenght)
    password = ''.join(list_of_symbols_for_password)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
notunderstanding_symbols = 'il1Lo0O'

approved_symbols = []

count_of_passwords = int(input('Сколько паролей необходимо создать? Напишите число'))
count_of_symbols = int(input('Сколько символов будет содержать пароль? Напишите число'))
include_digits = input('Будет ли пароль включать числа? Ответьте yes или no')
include_uppercase_alph = input('Будет ли пароль включать заглавные буквы? Ответьте yes или no')
include_lowercase_alph = input('Будет ли пароль включать строчные буквы? Ответьте yes или no')
include_punctuation = input('Будет ли пароль включать спецсимволы? Ответьте yes или no')
exclude_notunderstanding_symbols = input('Будем ли исключать из пароля непонятные символы? Ответьте yes или no')

if include_digits.lower() == 'yes':
    approved_symbols.extend(digits)

if include_uppercase_alph.lower() == 'yes':
    approved_symbols.extend(uppercase_letters)

if include_lowercase_alph.lower() == 'yes':
    approved_symbols.extend(lowercase_letters)

if include_punctuation.lower() == 'yes':
    approved_symbols.extend(punctuation)

if exclude_notunderstanding_symbols.lower() == 'yes':
    approved_symbols = [char for char in approved_symbols if char not in notunderstanding_symbols]


for passwords in range(count_of_passwords):
    password = generate_password(count_of_symbols, approved_symbols)
    print(password)