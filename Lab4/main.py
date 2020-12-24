import numpy as np

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


# print(main_table_sudoku2[1][1])

# for k in main_table_sudoku2:
#     print(k)

def matrix_show(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()


# matrix_show(main_table_sudoku2)

def structure_of_neighbours(i, j):
    array = np.zeros((9, 9), int)

    for k in range(len(array)):
        for m in range(len(array[k])):
            if k == i or m == j: array[k][m] = 1

    for k in range(3):
        for m in range(3):
            if i % 3 == k and j % 3 == m:
                for l in range(3):
                    for p in range(3):
                        array[i - k + l][j - m + p] = 1
    array[i][j] = 0
    print(array)


structure_of_neighbours(2, 3)
