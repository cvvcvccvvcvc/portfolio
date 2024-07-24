import random as r
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuatio = "!#$%&*+-=?@^_"

chars = ""

nuber_of_passwords = input("Количество паролей для генерации \n")
lenght_of_passwords = input("Длину одного пароля \n")
digits_enter = input("Включать ли цифры \n")
lowercase_enter = input("Включать ли прописные буквы \n")
uppercase_enter = input("Включать ли строчные буквы \n")
punctuatio_enter = input("Включать ли символы \n")
delete_some = input("Исключать ли неоднозначные символы \n")

if digits_enter.lower() == 'y':
    chars += digits
if lowercase_enter.lower() == 'y':
    chars += lowercase_letters
if uppercase_enter.lower() == 'y':
    chars += uppercase_letters
if punctuatio_enter.lower() == 'y':
    chars += punctuatio
if delete_some.lower() == 'y':
    for i in 'il1Lo0O':
        chars.replace(i,'')

def generate_password(lenght, chars):
    for i in range(int(nuber_of_passwords)):
        for k in r.sample(chars, lenght):
            print(k, sep="", end="")
        print()

generate_password(int(lenght_of_passwords), chars)