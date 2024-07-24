# set is like a list, but it can't have(!!!) duplicates     set() deletes duplicates when converts(!!!)
# AND SET is not iterable (порядок знаков не важен)  {1,2,3} == {3,1,2}
# Объединение множеств – множество, состоящее из элементов, принадлежащих хотя бы одному из объединяемых множеств
#пересечение; разность; симметрическая разность; дополнение.
# .add(1) добавляет единицу в set.  для удаления: .remove(1) удаляет единицу. Если единицы нет - ошибка
# .discard(1) то же самое что remove только без ошибки
# .pop() удаляет случайный элемент из set. Если список пустой - ошибка
# .clear() очищает сет
# порядок для обхода элементов (for) изменяется рандомно после изменений над set ом

# методы, в отличии от операторов могут принимать также список, строку, кортеж

# issuperset(), issubset(), isdisjoint(). первые два понятны (>, <, >=, <=). последний True если нет общих элементов.
test_set = set([1, 2, 2, 2, 5])   # set(arr) = 1, 2, 5
test_set2 = {1, 1, 1, 5, 8}

intersection = test_set & test_set2     # returns {values, that both set include}
# or
intersection = test_set.intersection(test_set2)
#or test_set.intersection_update(test_set2)  == test_set &= test_set2

union = test_set | test_set2
#or
union = test_set.union(test_set2)
#or test_set.update(test_set2)  == test_set |= test_set2

difference = test_set - test_set2
difference2 = test_set2 - test_set
#or
difference = test_set.difference(test_set2)
# difference_update() для изменения текущенго множества

symmetric_difference = test_set ^ test_set2
#or
symmetric_difference = test_set.symmetric_difference(test_set2)



print()
print("intesection of {1,2,5} and {8,1,5}:     ", intersection)
print()
print("union these sets:           ", union)
print()
print("difference betwen {1,2,5} and {8,1,5}:    ", difference)
print()
print("difference betwen {8,1,5} and {1,2,5}:    ", difference2)
print()
print()
print()
