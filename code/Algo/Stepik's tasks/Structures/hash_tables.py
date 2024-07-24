# hash function takes "sring" (number/string/smth) and gives number
# hash function + arrange = hash table
# Оператор in позволяет проверить, содержит ли словарь заданный КЛЮЧ.
book = dict()
book["apple"] = 0.87  
book["milk"] = 1.49
book["avocado"] = 1.49
print()
print("just print:", book)
print()
print("print by key (dict['']):    ", book["avocado"]) # call value by key: dict["str""]. CALL - [""]
print()

print("unpacked dict (*dict):       ", *book)  # upacking gives keys
print()
info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
info_dict = dict(info_list)  # создаем словарь на основе списка кортежей
dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information') # name: ... age:... job: Missed information ("" == None)

#   Методы .get() и setdefault()
print("method dict.GET(key, any return):     ", book.get("no", None))  # get returns value, if "tom" in keys, 
#                                                                        similarly to:  book["no"]   BUT there is not None (only Error!)   
#               if dict.get(el)  if sense True
book.setdefault("milk", 1.00)
print("method dict.setdefault(key, any value):     ", book)
print()

#      Методы keys(), values(), items()
print("method dict.ITEMS():    ", book.items())          #  returns список пары кортежей [(key1, value1), (key2, value2)]    некий объект представления 
print()
print("method dict.VALUES():         ", book.values())
print()
print("method dict.KEYS():         ", book.keys())    # returns keys in list [key1, key2, key3]           некий объект представления

print()

# method .update   -  конкатенация словарей. Главнее тот, который в аргументе
info1 = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}
info2 = {'age': 30,
        'city': 'New York',
        'email': 'bob@web.com'}
info1.update(info2)           # == info1 |= info2
print(info1)

print()

#  Методы удаления: оператор del, .pop, .popitem, .clear
del book["apple"] # if key not in arr, ERROR
milk = book.pop("milk", None) # simillary to .get and del.
avocado = book.popitem()   # удаляет последний добавленный элемент
book.clear() # понятно

# поверхностное и глубинное копирование
info_dict_copy = dict1.copy()  # создает новый элемент в памяти компа
info_dict_2 = dict1            # копирует ссылку на старый элемент

