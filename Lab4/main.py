from functional_sudoku import markup_search_algorithm as msa, deletion_algorithm as da, vertex_admissibility_q as vaq, \
    transition_to_real_num as t_trn, matrix_show as ms
import numpy as np
from time import perf_counter

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

"""
нерешаемое судоку3
"""
main_table_sudoku3 = \
    [
        [8, 1, 0, 0, 3, 0, 0, 2, 7],
        [0, 6, 2, 7, 5, 4, 3, 9, 1],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 6, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 5, 0, 7, 0],

        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 1, 0, 7, 5, 0],
        [0, 0, 0, 0, 7, 0, 0, 4, 2]
    ]


print('//---------------------------------------------//')
start = perf_counter()
print(t_trn(msa(da(vaq(main_table_sudoku1)))))
end = perf_counter()
print('//---------------------------------------------//')
print('Time of solution for the first sudoku: ', end - start)
print('//---------------------------------------------//')


start_ = perf_counter()
print(t_trn(msa(da(vaq(main_table_sudoku2)))))
end_ = perf_counter()
print('//---------------------------------------------//')
print('Time of solution for the second sudoku: ', end_ - start_)
print('//---------------------------------------------//')


"""
нерешаемое судоку3
"""
# start3 = perf_counter()
# print(t_trn(msa(da(vaq(main_table_sudoku3)))))
# end3 = perf_counter()
# print('//---------------------------------------------//')
# print('Time of solution for the second sudoku: ', end3 - start3)
# print('//---------------------------------------------//')
