import numpy as np
from time import sleep
from os import system

np.set_printoptions(edgeitems=30)
Z = np.random.randint(0, 2, [20, 20])
# for line in Z:
#     print(line)
with open('C:\\Users\\HYPER\\PycharmProjects\\Classes 4 wave\\saturday\\gSheetsExample\\numpy_datasets\\2', 'r') as f:
    # for line in f:
    Z = np.stack([np.fromiter(line.strip(), dtype=np.int8) for line in f])

def printZ(Z):
    # A = Z.copy().astype(str)
    # A[A=='0'] = ' '
    # A[A=='1'] = '*'
    for line in Z:
        str1 = ''.join(['*' if el==1 else ' ' for el in line])
        print(str1)

def generation(Z):
    b = np.zeros([Z.shape[0]+2, Z.shape[1]+2], dtype=np.int8)
    b[1:-1, 1:-1] = Z[...]
    b[1:-1, 0] = Z[:,-1]
    b[1:-1, -1] = Z[:, 0]
    b[0, 1:-1] = Z[-1, :]
    b[-1, 1:-1] = Z[0, :]
    b[0, 0] = Z[-1,-1]
    b[-1, -1] = Z[0,0]
    b[0, -1] = Z[-1, 0]
    b[-1, 0] = Z[0, -1]
    #Матрица соседей
    N = (b[0:-2,0:-2] + b[0:-2,1:-1] + b[0:-2,2:]
       + b[1:-1,0:-2]                + b[1:-1,2:]
       + b[2:,0:-2]   + b[2:,1:-1]   + b[2:,2:]  )
    # print(Z)
    # print(N)
    #Правило рождения
    birth = (Z==0) & (N==3)
    # print(birth)
    #Правило выживания
    survival = (Z==1) & ((N==2) | (N==3))
    # print(survival)
    #Правило жизни
    life = (birth|survival)
    # print(life)
    Z[...] = 0
    Z[life] = 1
    return Z

printZ(Z)

while(True):
    Z = generation(Z)
    sleep(0.04)
    system('cls')
    printZ(Z)
