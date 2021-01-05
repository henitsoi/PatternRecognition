import numpy as np
import json
import matplotlib.pyplot as plt


def summ_for_bigramm(list_, start, end):
    return sum([list_[j] for j in range(start, end)])


def bigramms_prob(path, first_letter, second_letter):
    with open(path, 'r') as f:
        data = json.load(f)
    print(data)

    lis_val, lis_key, lis_iterate = [], [], []

    for char in " abcdefghijklmnopqrstuvwxyz":
        iterator = 0
        for i, j in data.items():
            if i[0] == char:
                iterator += 1
                lis_val.append(j)
                lis_key.append(i)
        lis_iterate.append(iterator)

    print('Before: ', lis_val)
    print('Sorted: ', lis_key)

    it_start = 0
    it_end = 0
    for i in lis_iterate:
        it_end += i
        su = summ_for_bigramm(lis_val, it_start, it_end)
        for j in range(it_start, it_end):
            lis_val[j] /= su
        it_start += i

    print('After: ', lis_val)
    print(sum(lis_val))

    dictionary = dict(zip(lis_key, lis_val))
    print('Result: ', dictionary)
    return dictionary[first_letter + second_letter]


# print(bigramms_prob('data/frequencies.json', ' ', 'a'))


def standard_chars(path):
    my_img = plt.imread(path).astype(dtype='uint8')
    return my_img


print(standard_chars('data/alphabet/a.png'))
