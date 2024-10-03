# int search(int[] list, String item){
#     for(int i=0; i<list.length(), i++){
#         if(list[i]==item){
#     return i;
#     }
#     }
# }
#
# def search(list, item):
#     for i in range(0, len(list)):
#         if list[i]==item:
#             return i
#     return None
#
# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return None
#
# my_list = [1, 3, 5, 7, 9]
#
# print(search(my_list, 3))
# print(search(my_list, 6))


class Person:
    def __init__(self,name, phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber

persons=[
    Person("Akbar", "+998912334566"),
    Person("Bekzod", "+998912334577"),
    Person("Damir", "+998912334578"),
    Person("Elmar", "+998912334511"),
    Person("Umar", "+998912334523"),
]


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess.name == item:
            return mid
        if guess.name > item:
            high = mid - 1
        else:
            low = mid + 1

    return None



ind=binary_search(persons, "Damir")
print(ind)

if ind:
    print(persons[ind].name, persons[ind].phoneNumber)