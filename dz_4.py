# Напишите функцию для транспонирования матрицы

from typing import List


def show_matrix(mass: List[List[int]]) -> None:
    for r in mass:
        print(" ".join(str(element) for element in r))

def transpose_matrix(mass: List[List[int]]) -> List[List[int]]:
    rows = len(mass)
    column = len(mass[0])
    
    transposed_matrix = [[mass[j][i] for j in range(rows)] for i in range(column)]
    return transposed_matrix

matrix = (3, 4, 6), (7, 8, 3)
matrix_2 = transpose_matrix(matrix)
show_matrix(matrix)
print()
print()
show_matrix(matrix_2)

# -----------------------------------------------------------------
# import numpy as np
# a = np.array([[0, 1, 2], [4, 5, 6]])
# a = a.transpose()
# print(a)



# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def dictionary(**kwargs):
    name = dict()
    for key, value in kwargs.items():
        if isinstance(value, (int, float, str, list)):
            value = str(value)
        name[value] = key
    return name


print(dictionary(american='Bill', russian=['Ivan', 'Stepan', 'Igor']))

