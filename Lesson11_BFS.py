from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:  # Пока очередь не пуста...
        person = search_queue.popleft()  # Чеповек проверяется топько в том спучае,
        if not person in searched:  # еспи он не проверяпся ранее
            if person_is_seller(person):  # Проверяем, является ли этот человек продавцом манго
                print(person + " is а mango seller ! ")  # Да, это продавец манго
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False  # Если выполнение дошло до этой строки, значит, в очереди нет продавца манго



search("you")
