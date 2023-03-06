def Choice():
    print ("Выберите действие: 1 - добавить запись, 2 - выдать список заметок, 3 - прочитать заметку, ")
    print("4 - редактировать заметку, 5 - удалить заметку")
    return int(input())

def Choice_find():
    print ("Выберите действие: 1 - найти по фамилии")
    return int(input())

def id_input():
    return int(input('Введите индекс заметки: '))

def Name_input():
    return input('Введите заголовок: ')

def Description_input():
    return input('Введите описание: ') # тело заметки

def Find(a):
    print ("Введите поисково слово: ")
    if (a != 3):
        return input()
    else:
        return int(input())
