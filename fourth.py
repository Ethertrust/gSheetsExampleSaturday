from datetime import datetime
# not and or in : True/False
# not - отрицание утверждения
# and - "и" истинно несколько утверждений
# or  - "или" истинно хотя бы одно из утверждений
# in  - проверка, что определенный элемент входит в набор элементов

hum1 = {'Имя': 'Василий'}
hum2 = {'Имя': 'Игорь', 'Age': 28}
hum3 = {'Имя': 'Василий', 'Age': 28}
hum4 = {'Имя': 'Василий', 'Age': 28}
# print(hum2['Age'])
hums = [hum1, hum2, hum3]

#Прогнать всех, кому не 30 лет
# if  hum1['Age'] != 30:
#     print("Проваливай!")

# if  not (False): #False -> True, True -> False
#     print("True")
# if  not (True): #False -> True, True -> False
#     print()
# else:
#     print("False")

# Прогнать всех Василиев 42 лет
# for hum in hums:
#     if hum['Имя'] == 'Василий':
#         if hum['Age'] == 42:
#             print('Проваливай!')

# for hum in hums:
#     if 'Age' in hum and hum['Age'] == 42 and hum['Имя'] == 'Василий':
#         print('Проваливай', hum['Имя'] + '!')

# Прогнать всех, кто является Василием, или младше 30 лет
# for hum in hums:
#     if hum['Имя'] == 'Василий' or hum['Age'] < 30:
#         print('Проваливай', hum['Имя'] + '!')

# if 1 in [1,2,3,4]:
#     print('1 найдена')
# else:
#     print('1 не найдена')

# if hum4 in hums:
#     print('Он там есть')
#     print(hums)
# else:
#     print('Его там нет')

if 'Василий' in 'ВасилийИгорь':
    print('Василий найден')
else:
    print('Василий не найден')

#datetime
# Создание строк с представлением даты
date_time_str = '18/09/19 01:55:19'
date_time_str2 = '28/09/18 23:55:00'
#>, >=
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
date_time_obj2 = datetime.strptime(date_time_str2, '%d/%m/%y %H:%M:%S')
print(date_time_obj, type(date_time_obj))
print(date_time_obj2, type(date_time_obj))
if date_time_obj > date_time_obj2:
    print(date_time_str, 'позднее, чем', date_time_str2)
else:
    print(date_time_obj2.strftime("%d/%m/%y %H:%M:%S"), 'позднее, чем', date_time_obj.strftime("%d/%m/%y %H:%M:%S"))