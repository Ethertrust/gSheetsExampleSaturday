# a = 0
# print(a)
# a +=1
# print(a)
# a +=1
# print(a)
# a +=1
# print(a)
# a +=1
# print(a)
# [0, 1, 2, 3, 4]
print('----------------0. Циклы')
# Правила идентации:
# 1. В каждом блоке инструкций каждая инструкция имеет одинаковый отступ с начала строки.
# 2. По завершении блока инструкций программа возвращается на предыдущий уровень инсрукций.
# for a in range(5):
#     print(a)
#     for b in range(3):
#         print(b)
#         print('Конец итерации вложенного цикла')
#     print('Конец итерации цикла')
# print('Конец цикла')
# Типы данных:
#   immutable(неизменяемые):
#       int - целые числа
#       float - вещественные числа
#       str - строка / упорядоченный набор символов
#       bool - логический тип данных: True:False / Истина:Ложь / (Всё, кроме нуля):(0)
#       tuple - упорядоченный набор элементов
#   mutable(изменяемые):
#       list / список - упорядоченный (набор элементов)/(контейнеры)
#       dict / словарь - неупорядоченный набор элементов index -> key
print('----------------1. Списки')
# list1 = [16, 17, 18, 19]
# print(list1, type(list1))
# print(list1[-1])
# print(list1[0], type(list1[0]))
# print(list1[0:1], type(list1[0:1]))
# print('4e' + '4e')
# print(list1 + [2,3,4])
# list1 = ['s', ',', 'o']
# print(' '.join(list1), type(' '.join(list1)))
# str1 = 'Привет мир!'
# list1 = str1.split()
# print(list1)
# for el in list1:
#     print(el)
# for el in str1:
#     print(el)
# list1[0] = 'Новый'
# print(list1)
# print(' '.join(list1))
# print(str1)
# a = 5
# b = 6
# str1 = 'Привет!'
# list1 = [a, b, str1]
# print(list1)
# list2 = [15, 16, list1]
# print(list2)
# list1 = [1, 2, 3]
# print(list2)
# print(list2[-1])
# list3=list2[-1]
# list3[-1] = 'Новый мир!'
# print(list2)
print('----------------2. Кортеж/ tuple')
# tuple1 = (1, 2, list1)
# print(tuple1)
# # tuple1[-1] = list2
# tuple1[-1][1] = 5
# print(tuple1)
print('----------------3. Словарь/ dict')
dict1 = {'Фамилия':'Иванов', 'Имя':'Иван', 'Отчество':'Иванович', 'Дата рождения':'19.01.2000'}
# print(dict1, type(dict1))
#print(dict1['Фамилия':'Дата рождения'])
# for el in dict1:
#     dict1[el] = '##############'
#     print(el, dict1[el])
dict1['Возраст'] = 26
print(dict1)
print('----------------3. Условные конструкции/ Ветвление')
# a = 6
# if a<7:
#     print('a<7')
# elif a==7:
#     print('a=7')
# elif a>7:
#     print('a>7')
print('Конец конструкции')
print('----------------4. Тернарное представление условных конструкций и циклов')
# print('Условные конструкции')
# print('a<7') if a<7 else print('a>=7')
# print('Циклы')
# list4 = [el+3 for el in list1]
# print(list4)
print('----------------5. Циклы с контйнерами')
# for el in list2:
#     print(el)
# for el in dict1:
#     print(el, dict1[el])
# for value in dict1.values():
#     print(value)
# for el, value in dict1.items():
#     print(el , value)
print('----------------6. Отладчик / debugger')
# Состояние программы - память программы: данные, и исполняемая строка кода.
dict2 = {'Фамилия':'Петров', 'Имя':'Петр', 'Отчество':'Петрович', 'Дата рождения':'19.01.2005'}
list5 = [dict1,dict2]
# dict2['Возраст'] = 19
for el in list5:
    if 'Возраст' in el:
        if el['Возраст'] > 20:
            print(el)

