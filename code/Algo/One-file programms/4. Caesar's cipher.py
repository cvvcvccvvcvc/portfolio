eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

way = input("Напишите команду. \n 1. шифруй \n 2. расшифруй \n 3. узнать шаг \n")

text = input("Введите текст, который вы хотите зашифровать/дешифровать")

direction = input("Введите направление сдвига. r/l")
language = input("Введите язык шифруемого/расшифруемого текста. ru/en")
shift = int(input("Введите шаг сдвига"))

def encryption(text, direction, language, shift):
    encrypted_text = ""
    if language == "ru":
        if direction == "r":
            for i in text:
                if i.isupper():
                    encrypted_text += rus_upper_alphabet[-32 + rus_upper_alphabet.find(i) + shift]
                elif i.islower():
                    encrypted_text += rus_lower_alphabet[-32 + rus_lower_alphabet.find(i) + shift]
                else:
                    encrypted_text += i
        elif direction == "l":
            for i in text:
                if i.isupper():
                    encrypted_text += rus_upper_alphabet[rus_upper_alphabet.find(i) - shift]
                elif i.islower():
                    encrypted_text += rus_lower_alphabet[rus_lower_alphabet.find(i) - shift]
                else:
                    encrypted_text += i
    if language == "en":
        if direction == "r":
            for i in text:
                if i.isupper():
                    encrypted_text += eng_upper_alphabet[-26 + eng_upper_alphabet.find(i) + shift]
                elif i.islower():
                    encrypted_text += eng_lower_alphabet[-26 + eng_lower_alphabet.find(i) + shift]
                else:
                    encrypted_text += i
        elif direction == "l":
            for i in text:
                if i.isupper():
                    encrypted_text += eng_upper_alphabet[eng_upper_alphabet.find(i) - shift]
                elif i.islower():
                    encrypted_text += eng_lower_alphabet[eng_lower_alphabet.find(i) - shift]
                else:
                    encrypted_text += i
    return encrypted_text

def decryption(text, direction, language, shift):
    decrypted_text = ""
    if language == "ru":
        if direction == "l":
            for i in text:
                if i.isupper():
                    decrypted_text += rus_upper_alphabet[-32 + rus_upper_alphabet.find(i) + shift]
                elif i.islower():
                    decrypted_text += rus_lower_alphabet[-32 + rus_lower_alphabet.find(i) + shift]
                else:
                    decrypted_text += i
        elif direction == "r":
            for i in text:
                if i.isupper():
                    decrypted_text += rus_upper_alphabet[rus_upper_alphabet.find(i) - shift]
                elif i.islower():
                    decrypted_text += rus_lower_alphabet[rus_lower_alphabet.find(i) - shift]
                else:
                    decrypted_text += i
    if language == "en":
        if direction == "l":
            for i in text:
                if i.isupper():
                    decrypted_text += eng_upper_alphabet[-26 + eng_upper_alphabet.find(i) + shift]
                elif i.islower():
                    decrypted_text += eng_lower_alphabet[-26 + eng_lower_alphabet.find(i) + shift]
                else:
                    decrypted_text += i
        elif direction == "r":
            for i in text:
                if i.isupper():
                    decrypted_text += eng_upper_alphabet[eng_upper_alphabet.find(i) - shift]
                elif i.islower():
                    decrypted_text += eng_lower_alphabet[eng_lower_alphabet.find(i) - shift]
                else:
                    decrypted_text += i
    return decrypted_text

def encryption_n(text, direction, language):
    for i in range(0, 25):
        print(i, end=":   ")
        print(encryption(text, direction, language, i))

def encryption_by_word(text, direction, language):
    list_words = text.split(" ")
    total_letters = 0
    for k in list_words:
        for i in k:
            if i.isalpha():
                total_letters += 1
        print(encryption(k, direction, language, total_letters), end=" ")
        total_letters = 0

if way == "шифруй":
    print(encryption(text, direction, language, shift))
elif way == "расшифруй":
    print(decryption(text, direction, language, shift))
elif way == "узнать шаг":
    encryption_n(text, direction, language)
elif way == "шифруй по слову":
    encryption_by_word(text, direction, language)

# НАДО СЧИТАТЬ БУКВЫ, НО НЕ УДАЛЯТЬ ЗНАКИ ПУНКТУАЦИИ. ПОТОМ СДЕЛАЮ
