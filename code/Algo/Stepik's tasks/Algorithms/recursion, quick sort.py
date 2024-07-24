

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])
    
def count_elements(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + count_elements(list[1:])
    
def find_biggest(list):
    biggest = 0
    if len(list) == 0:
        return biggest
    else:
        if list[-1] > biggest:
            biggest = list[-1]
        list.pop()
        if biggest > find_biggest(list):
            return biggest
        else:
            return find_biggest(list)

def biggest2(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    suggest_big = biggest2(list[1:])
    return list[0] if list[0] > suggest_big else suggest_big

from random import randrange
def qsort(arr):
    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        return [arr[1], arr[0]] if arr[0] > arr[1] else [arr[0], arr[1]]
    elif len(arr) > 2:
        main = arr[randrange(len(arr))]
        new_arr = arr[:arr.index(main)] + arr[arr.index(main) + 1:]
        who_big = [i for i in new_arr[0:] if i >= main]
        who_low = [i for i in new_arr[0:] if i < main]
        return qsort(who_low) + [main] + qsort(who_big)


print(qsort([21, 2, 3, 522, 1111, 55]))