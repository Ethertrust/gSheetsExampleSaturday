import numpy as np

list3 = [1, 2]
scores_l = [[20, 40, 56, 80, 0, 5, 25, 27, 74, 1],
         [0, 98, 67, 100, 8, 56, 34, 82, 100, 7],
         [78, 54, 23, 79, 100, 0, 0, 42, 95, 83],
         [51, 50, 47, 23, 100, 94, 25, 48, 38, 77],
         [90, 87, 41, 89, 52, 0, 5, 17, 28, 99],
         [32, 18, 21, 18, 29, 31, 48, 62, 76, 22],
         [6, 0, 65, 78, 43, 22, 38, 88, 94, 100]]
scores = np.array(scores_l)

list1 = [[1, 2],
         [4, 5],
         [3, 6]]
print(list1, type(list1))
a = np.array(list1)
print(a, type(a))
print('-------------')
print('1. основные свойства Numpy массивов')
print('Размерность массива:',a.ndim)
print('Размер массива:',a.size)
print('Размер массива:',a.shape)
print('тип данных массива:',a.dtype)
print('-------------')
print('2. Создание Numpy массивов')
print([[1, 2, 3],
             [4, 5, 6]])
b = np.array([[1, 2, 3],
             [4, 5, 6]])
print(b)
b = np.zeros([2,3,2])
print(b, b.dtype)
print(np.ones([2,3]))
print(np.full([2,3], 8))
print(np.full_like(b, 9))
print(np.eye(6, dtype=np.int32))
print(np.random.rand(6, 5) * 6 - 3)
print(np.random.randint(6, 13, [3, 3]))
b = np.array([[1, 2, 3],
             ['a', 5, 6]], dtype=object)
print(b)
print('-------------')
print('3. Нарезка Numpy массивов')
print(scores)
print(scores[-1])
print(scores[-1][-2])
print(scores[-1, -2])
print(scores[-1, -2:])
print(scores[-2:, -2:])
print('-------------')
print('4.Булевы Numpy массивы')
print(scores, scores.shape)
c = scores>50
print(c, scores.shape)
print(scores[c])
print('-------------')
print('5.Операции с Numpy массивами')
b = np.array([[1, 2, 3],
             [4, 5, 6],
              [4, 5, 6]])
d = np.full_like(b, 3)
print(b)
print(d)
# print(b * d)
# list1 = [[1, 2],
#          [4, 5],
#          [3, 6]]
# c = np.array(list1)
# print(b @ c)
# print(b - d)
#print(b - c) # Разные размеры не допустимы
#print(b + c) # Разные размеры не допустимы
# print(b/d)
t = np.power(b, 2)
print(t)
t = np.power(b, d)
print(t)
T = t.T
print(T)
print('-------------')
print('6.Стандартные функции модуля Numpy')
print(scores)
print(scores.min())
print(scores.min(axis=0))
# print(scores.min(axis=1))
# ddd = np.array([[[1, 2, 3],
#              [4, 5, 6]],
#               [[7, 8, 9],
#                [10, 11, 12]]])
# print(ddd)
# print(ddd[1,0,1])
# print(ddd.min(axis=0))
# print(ddd.min(axis=1))
# print(ddd.min(axis=2))
# print(scores.max(axis=0))
# help(np.min)
print(scores.argmin(axis=0))
a = np.array([0, 90, 30])
print(a)
print(np.sin(np.deg2rad(a))) # sin, как и все триганометрические функции принимают радианы
print(np.exp(a))
print('-------------')
print('7.Массивы Numpy с множеством измерений')
cube1 = np.random.randint(1, 3, [3,3,3])
cube2 = np.random.randint(3, 5, [3,3,3])
cube3 = np.random.randint(5, 7, [3,3,3])
print(cube1)
q1 = np.array([cube1, cube2, cube3])
q2 = np.array([cube3, cube2, cube1])
q3 = np.array([cube2, cube3, cube1])
arr = np.array([q1, q2, q3])
print(arr)
print(arr.shape)
print(arr[1])
print(arr[1,:,:,:,0])
print(arr[1,2,...,0])
# print(arr[1,2,...,0,...])
print(arr[1,2,0,...])
print(arr[...,1,2,0])


