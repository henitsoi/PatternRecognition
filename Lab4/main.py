import numpy as np
import pandas as pd

main_table_sudoku1 = \
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],

        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],

        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

main_table_sudoku2 = \
    [
        [8, 1, 0, 0, 3, 0, 0, 2, 7],
        [0, 6, 2, 0, 0, 0, 0, 9, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 6, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 5, 0, 7, 0],

        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 1, 0, 7, 5, 0],
        [0, 0, 0, 0, 7, 0, 0, 4, 2]
    ]


def matrix_show(array):
    return pd.DataFrame(np.array([array[i][j] for i in range(len(array)) for j in range(len(array[i]))]).reshape(9, 9),
                        columns=['c_0', 'c_1', 'c_2', 'c_3', 'c_4', 'c_5', 'c_6', 'c_7', 'c_8']) \
        if len(array) > 0 else 0


print('//---------------------------------------------//')
print(matrix_show(main_table_sudoku1))


def check_for_good_markup(massive):
    array_ = np.array(massive)
    row, col = array_.shape[0], array_.shape[1]

    check_markup = [(i + 1) * 10 + j + 1 for i in range(row) for j in range(col) if array_[i][j].sum() == 0]

    # print('Full non Admissibility cells: ', len(check_markup))
    return 0 if len(check_markup) > 0 else 1


# print(check_for_good_markup(vertex_admissibility_q(main_table_sudoku1)))

def transition_to_real_num(array):
    supporting_array = np.zeros((9, 9), dtype=np.uint8)
    row, col, num = array.shape[0], array.shape[1], array.shape[2]

    for i in range(row):
        for j in range(col):
            check = 0
            for k in range(num):
                check += array[i][j][k]
            if check == 1:
                supporting_array[i][j] = np.nonzero(array[i][j])[0][0] + 1
    return pd.DataFrame(supporting_array, columns=['c_0', 'c_1', 'c_2', 'c_3', 'c_4', 'c_5', 'c_6', 'c_7', 'c_8'])


def vertex_admissibility_q(massive):
    supporting_q_array = np.ones((9, 9, 9), dtype=np.uint8)
    array_ = np.array(massive).reshape(81, )
    b = 0

    for k in range(array_.shape[0]):
        if array_[k] != 0:
            kappa = array_[k]
            for i in range(supporting_q_array.shape[2]):
                if kappa != i + 1:
                    supporting_q_array[b][k % 9][i] = 0
        if (k + 1) % 9 == 0: b += 1

    return supporting_q_array


# print('//---------------------------------------------//')
# print(vertex_admissibility_q(main_table_sudoku1))
print('//---------------------------------------------//')


def structure_of_neighbours_g(i, j):
    array = np.zeros((9, 9), dtype=np.uint8)
    row, col = array.shape[0], array.shape[1]

    for k in range(row):
        for m in range(col):
            if k == i or m == j: array[k][m] = 1

    for k in range(int(row / 3)):
        for m in range(int(col / 3)):
            if i % 3 == k and j % 3 == m:
                for l in range(int(row / 3)):
                    for p in range(int(col / 3)):
                        array[i - k + l][j - m + p] = 1
    array[i][j] = 0
    return pd.DataFrame(array, columns=['c_0', 'c_1', 'c_2', 'c_3', 'c_4', 'c_5', 'c_6', 'c_7', 'c_8'])


# print('//---------------------------------------------//')
print(structure_of_neighbours_g(0, 1))
print('//---------------------------------------------//')


def deletion_algorithm(massive):
    massive_ = massive.copy()
    row, col, num = massive.shape[0], massive.shape[1], massive.shape[2]

    for i in range(row):
        for j in range(col):
            check = 0
            for m in range(num):
                check += massive[i][j][m]
            if check == 1:
                data = np.array(structure_of_neighbours_g(i, j))
                # выбираем индекс ненулевого элемента в заполненом обьекте
                index_nonzero_element = np.nonzero(massive[i][j])[0][0]
                for k in range(row):
                    for n in range(col):
                        if data[k][n] == 1:
                            # зануляем метку, которая соответсвует индексу выбранной, во всех соседях
                            massive[k][n][index_nonzero_element] = 0
    if check_for_good_markup(massive) == 0:
        print('Unreal to solve!!!')
    elif massive.sum() == 81:
        print('We have one solve!!!')
    elif massive.sum() > 81:
        if (massive_ == massive).all():
            print('Now only the markup search algorithm will help us...')
            return massive
        print('We need to use one more time deletion_algorithm')
        deletion_algorithm(massive)
    # print('Admissibility q = ', massive.sum())
    return massive


res = deletion_algorithm(vertex_admissibility_q(main_table_sudoku1))
# print(res)
# print(check_for_good_markup(res))
print('//---------------------------------------------//')
print(transition_to_real_num(res))
print('//---------------------------------------------//')
