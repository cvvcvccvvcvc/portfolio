import random as r

words_list = [
    "человек",
    "слово",
    "лицо",
    "дверь",
    "земля",
    "работа",
    "ребенок",
    "история",
    "женщина",
    "развитие",
    "власть",
    "правительство",
    "начальник",
    "спектакль",
    "автомобиль",
    "экономика",
    "литература",
    "граница",
    "магазин",
    "председатель",
    "сотрудник",
    "республика",
    "личность",
]


def get_word(words):
    return r.choice(words).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ ⎞
                   |    
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ 
                   |
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |
                   |
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     ⎛▼
                   |
                   |
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      ▼
                   |
                   |
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


word = get_word(words_list)


def play(word):
    word_completion = "_" * len(
        word
    )  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    print("Давайте играть в угадайку слов!")
    while tries != 0 and guessed == False:
        print(display_hangman(tries))
        print(f"Осталось попыток = {tries}")
        print(f"Загаданное слово {word_completion}")
        print("Предположите букву или слово")
        guess = input()
        while guess.isdigit() or not guess.isalpha():
            print("Вводите только буквы/слова!")
            guess = input()
        if guess.upper() in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            guessed_letters.append(guess)
            if guess in word:
                print(f"Поздравляю! вы угадали букву {guess}")
                word_completion = (
                    word_completion[: word.find(guess)]
                    + guess
                    + word_completion[word.find(guess) + 1 :]
                )
            else:
                print("К сожалению, вы не угадали!")
                print("Буквы которые вы уже пробовали:")
                print(guessed_letters)
                tries -= 1
                if tries == 0:
                    print(f"""Вы лузер!!! загадано было слово {word}!!!""")
                    print()
                    again = input("Хотите сыграть еще раз?")
                    if again == "y":
                        word = get_word(words_list)
                        tries = 6
        else:
            guessed_words.append(guess)
            if guess == word:
                print(f"Поздравляю! вы угадали слово {guess}")
                guessed = True
            else:
                print("К сожалению, вы не угадали!")
                print(guessed_words)
                tries -= 1
                if tries == 0:
                    print(f"""Вы лузер!!! загадано было слово {word}!!!""")
                    print()
                    again = input("Хотите сыграть еще раз?")
                    if again == "y":
                        word = get_word()
                        tries = 6


play(word)
