import numpy as np
from json import load
from matplotlib.pyplot import imread
from os.path import splitext
from os import walk


def sum_for_bigramm(list_, start, end):
    """
    >>> sum_for_bigramm([1,2,3,4,5,6,7,8,9], 0, 4)
    10
    """
    return sum([list_[j] for j in range(start, end)])


def bigramms_prob(path, first_letter, second_letter):
    with open(path, 'r') as f:
        data = load(f)
    lis_val, lis_key, lis_iterate = [], [], []

    for char in " abcdefghijklmnopqrstuvwxyz":
        iterator = 0
        for i, j in data.items():
            if i[0] == char:
                iterator += 1
                lis_val.append(j)
                lis_key.append(i)
        lis_iterate.append(iterator)

    it_start = 0
    it_end = 0

    for i in lis_iterate:
        it_end += i
        su = sum_for_bigramm(lis_val, it_start, it_end)
        for j in range(it_start, it_end):
            lis_val[j] /= su
        it_start += i

    dictionary = dict(zip(lis_key, lis_val))
    return dictionary[first_letter + second_letter]


def name_file_in_alphabet(path):
    fl = []
    for base in [filename for filename in walk(path)][0][2]:
        fl.append(splitext(base)[0])
    return fl


def standard_chars(const_string_name):
    list_ = name_file_in_alphabet(const_string_name)
    dictionary = {}
    for i in list_:
        my_img = imread(const_string_name + '/' + i + '.png').astype(dtype='uint8')
        dictionary[i] = my_img
    dictionary[' '] = dictionary.pop('space')
    return dictionary


def x_picture_char_dictionary(path, const_path):
    my_img = imread(const_path + path).astype(dtype='uint8')
    height, width_with_n_char = my_img.shape
    width = height
    count_of_char = int(width_with_n_char / height)
    dictionary = {}

    for i in range(count_of_char):
        test_array = my_img[:, width * i:width * (i + 1)]
        dictionary[i] = test_array
    return dictionary, count_of_char


def q_part(x_char, standard_char_massive, noise_level):
    """
    >>> q_part(np.array([1,0,0,1,0,1,0]), np.array([1,1,0,1,1,1,0]), 0)
    5
    >>> q_part(np.array([1,0,0,1,0,1,0]), np.array([1,1,0,1,1,1,0]), 1)
    2
    """
    if noise_level == 0:
        return np.array(x_char == standard_char_massive).sum()
    elif noise_level == 1:
        return np.array(x_char != standard_char_massive).sum()
    else:
        return \
            np.array(x_char != standard_char_massive).sum() * np.log(noise_level) + np.array(
                x_char == standard_char_massive).sum() * np.log(1 - noise_level)


def f_part(path_for_bigramms, x_char_dictionary, iterat, standard_chars_dictionary, first_char, noise_level, flag,
           result_prev_f_part, flag2):
    dictionary, it = {}, 0
    for i, j in standard_chars_dictionary.items():
        if flag == 1:
            try:
                dictionary[i] = np.log(bigramms_prob(path_for_bigramms, first_char, i)) + q_part(
                    x_char_dictionary[iterat], j, noise_level)
            except (KeyError, TypeError):
                pass
        else:
            try:
                dictionary[i] = np.log(bigramms_prob(path_for_bigramms, first_char, i)) + q_part(
                    x_char_dictionary[iterat], j, noise_level) + result_prev_f_part[i]
            except (KeyError, TypeError):
                pass
        it += 1
    if flag2 == 1:
        v_val = list(dictionary.values())
        k_key = list(dictionary.keys())
        return k_key[v_val.index(max(v_val))]
    return max(dictionary.values())


def r_part(path_for_bigramms, x_char_dictionary, counts_of_letters, standard_chars_dictionary, noise_lvl):
    dictionary = {}
    for i in range(counts_of_letters):
        counter_ = counts_of_letters - i - 1
        dictionary[i] = {}
        for j in standard_chars_dictionary.keys():
            if i == 0:
                dictionary[i][j] = f_part(path_for_bigramms, x_char_dictionary, counter_,
                                          standard_chars_dictionary, j, noise_lvl, 1, 0, 0)
            else:
                dictionary[i][j] = f_part(path_for_bigramms, x_char_dictionary, counter_,
                                          standard_chars_dictionary, j, noise_lvl, 0, dictionary[i - 1], 0)
    return dictionary


def k_last_part(path_for_bigramms, x_char_dictionary, counts_of_letters, standard_chars_dictionary, noise_lvl):
    dictionary = r_part(path_for_bigramms, x_char_dictionary, counts_of_letters, standard_chars_dictionary, noise_lvl)
    gl_list = [' ']

    for i in range(counts_of_letters - 1, -1, -1):
        counter_ = counts_of_letters - i - 1
        if i == 0:
            tmp = f_part(path_for_bigramms, x_char_dictionary, counter_, standard_chars_dictionary,
                         gl_list[counter_], noise_lvl, 1, 0, 1)
        else:
            tmp = f_part(path_for_bigramms, x_char_dictionary, counter_, standard_chars_dictionary,
                         gl_list[counter_], noise_lvl, 0, dictionary[i - 1], 1)
        gl_list.append(tmp)
    print(' '.join(gl_list))


if __name__ == '__main__':
    import doctest

    doctest.testmod()