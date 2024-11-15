from os import listdir
from os.path import isfile, join
from collections import deque


def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)  # Если это файл, вывести его имя
            else:
                search_queue.append(fullpath)


#printnames("pics")



def printnames_recursive(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file) #Если это файл, вывести его имя
        else:
            printnames_recursive(fullpath)
printnames_recursive("pics")