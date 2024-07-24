l = sorted(["Иванов", "Петров", "Сидоров", "Амбалов", "Лысов", "Баранов", "Лунегов", "Латина", "Костина",
     "Монеткина", "Платонова", "Никандров", "Родыгина", "Боброва", "Крыжовникова", "Балабаева", "Осипова"])
# задача: максимально быстро найти фамилию в телефонной книге. Дано: Фамилия. Вывод: индекс фамилии
surname = input()
from math import ceil
def compare_alphabet(surname, suggest):  #1 = sur bigger, -1 - sur lower, 0 - surname match!
     alphabet = [*"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower()]
     if surname == suggest:
          return 0
     if alphabet.index(surname[0].lower()) > alphabet.index(suggest[0].lower()):
          return 1
     elif alphabet.index(surname[0].lower()) < alphabet.index(suggest[0].lower()):
          return -1
     if surname[0] == suggest[0]:
          if alphabet.index(surname[1].lower()) > alphabet.index(suggest[1].lower()):
               return 1
          elif alphabet.index(surname[1].lower()) < alphabet.index(suggest[1].lower()):
               return -1

def binary_search(surname, l):
     high = len(l) - 1
     print(high)
     low = 0
     while low <= high:
          mid = ceil((high + low)/2)
          suggest = l[mid]
          if compare_alphabet(surname, suggest) == 1:
               low = mid + 1
               return mid
          elif compare_alphabet(surname, suggest) == 0:
               return mid
          else:
               high = mid - 1
          print(f"low={low}, high={high}, mid={mid}")
     return 1
          
print(l)
print(binary_search(surname, l))

