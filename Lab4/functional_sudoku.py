import numpy as np
import pandas as pd


def matrix_show(array):
    return pd.DataFrame(np.array([array[i][j] for i in range(len(array)) for j in range(len(array[i]))]).reshape(9, 9),
                        columns=['c_0', 'c_1', 'c_2', 'c_3', 'c_4', 'c_5', 'c_6', 'c_7', 'c_8']) \
        if len(array) > 0 else 0


def check_for_good_markup(massive):
    """
    >>> check_for_good_markup(np.array([[[1,0,0,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0]],[[0,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,\
    0,0]]]))
    0
    >>> check_for_good_markup(np.array([[[1,0,0,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0]],[[0,1,1,1,1,1,1,1,0],[0,0,1,0,0,0,0,\
    0,0]]]))
    1
    """
    array_ = np.array(massive)
    row, col = array_.shape[0], array_.shape[1]

    check_markup = [(i + 1) * 10 + j + 1 for i in range(row) for j in range(col) if array_[i][j].sum() == 0]

    # print('Full non Admissibility cells: ', len(check_markup))
    return 0 if len(check_markup) > 0 else 1


def sum_check(array, i, j, num):
    check = 0
    for m in range(num):
        check += array[i][j][m]
    return check


def transition_to_real_num(array):
    supporting_array = np.zeros((9, 9), dtype=np.uint8)
    row, col, num = array.shape[0], array.shape[1], array.shape[2]

    for i in range(row):
        for j in range(col):
            if sum_check(array, i, j, num) == 1:
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
        if (k + 1) % 9 == 0:
            b += 1
    return supporting_q_array


def structure_of_neighbours_g(i, j):
    array = np.zeros((9, 9), dtype=np.uint8)
    row, col = array.shape[0], array.shape[1]

    for k in range(row):
        for m in range(col):
            if k == i or m == j:
                array[k][m] = 1

    for k in range(int(row / 3)):
        for m in range(int(col / 3)):
            if i % 3 == k and j % 3 == m:
                for l in range(int(row / 3)):
                    for p in range(int(col / 3)):
                        array[i - k + l][j - m + p] = 1
    array[i][j] = 0
    return pd.DataFrame(array, columns=['c_0', 'c_1', 'c_2', 'c_3', 'c_4', 'c_5', 'c_6', 'c_7', 'c_8'])


def deletion_algorithm(massive):
    massive_ = massive.copy()
    row, col, num = massive.shape[0], massive.shape[1], massive.shape[2]

    for i in range(row):
        for j in range(col):
            if sum_check(massive, i, j, num) == 1:
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
        return massive
    elif check_for_good_markup(massive) == 1 and massive.sum() == 81:
        print('//---------------------------------------------//')
        print('We have one solution!!!')
        return massive
    elif check_for_good_markup(massive) == 1 and massive.sum() > 81:
        if (massive_ == massive).all():
            print('Now only the markup search algorithm will help us...')
            print(transition_to_real_num(massive))
            return massive
        print('We need to use one more time deletion_algorithm')
        deletion_algorithm(massive)
    return massive


def markup_search_algorithm(array):
    row, col, num = array.shape[0], array.shape[1], array.shape[2]
    data = deletion_algorithm(array)

    if check_for_good_markup(data) == 1 and data.sum() == 81:
        return array

    for i in range(row):
        for j in range(col):
            if sum_check(array, i, j, num) > 1:
                array_ = array.copy()
                index_nonzero_elements = np.nonzero(array[i][j])[0]
                for count in index_nonzero_elements:
                    for k in index_nonzero_elements:
                        if count != k:
                            array[i][j][k] = 0
                    arr_aft_del_alg = array_
                    arr_aft_del_alg_ = deletion_algorithm(array)
                    if (arr_aft_del_alg == arr_aft_del_alg_).all():
                        return array
                    elif check_for_good_markup(arr_aft_del_alg_) == 0:
                        array = array_
                    else:
                        array = arr_aft_del_alg_
                        break
    return array


if __name__ == '__main__':
    import doctest

    doctest.testmod()
