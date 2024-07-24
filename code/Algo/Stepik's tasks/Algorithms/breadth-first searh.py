# поиск в ширину постоянно увеличивает базу рассматриваемых объектов
# есть 2 типа: поиск кратчайшего пути от узла А к В   и поиск существует ли путь между узлами А и В
# существует структура данных хорошо подходящая под поиск кратч. пути   -  очереди  (2 операции: постановка в конец, извлечение из начала)
# works with directed unweighted graphs

graph = {}
graph["you"] = ["Martin", "Pidor", "Maxim", "Alice"]
graph["Martin"] = ["Pidor", "Clare"]
graph["Pidor"] = []
graph["Maxim"] = ["Pidor"]
graph["Alice"] = ["Pidor"]
graph["Clare"] = ["Sarah"]
graph["Sarah"] = []
# is order of adding important? NO
# it is DIRECTED GRAPH (1 arrow  or 2 in cyclce),   also there is undirected graph (no arrows / 2 arrows) 

# we need to make order. В питоне есть двусторонняя очередь (дека) deque
from collections import deque

def person_is_good(name):
    return name[-1] == "h"
# нужно учесть что 2 раза провреять одного чела не надо. Иначе лишняя работа + риск бесконенчого цикла                    
def search(first_man):
    search_deque = deque()
    search_deque += graph[first_man]
    check_list = []
    while search_deque:
        person = search_deque.popleft()
        if person not in check_list:
            if person_is_good(person):
                print("Good person is " + person + "!")
                return True
            else:
                check_list.append(person)
                search_deque += graph[person]
        else:
            continue
    return False

print(search("you"))