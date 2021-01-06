from func import k_last_part, x_picture_char_dictionary, standard_chars
from time import perf_counter
import numpy as np
from time import sleep


def inside(testnum, beginRange, endRange):
    return beginRange < testnum < endRange


const_str_path_to_input = 'data/input/'
const_str_path_to_json = 'data/frequencies.json'
const_string_alphabet = 'data/alphabet'
const_string_x = 'very simple text_0.7.png'
const_string_x1 = 'but thence i learn and find the lesson true drugs poison him that so feil sick of you_0.4.png'

const_str_file_massive = np.array([
    ['but thence i learn and find the lesson true drugs poison him that so feil sick of you_0.3.png'],
    ['but thence i learn and find the lesson true drugs poison him that so feil sick of you_0.4.png'],
    ['but thence i learn and find the lesson true drugs poison him that so feil sick of you_0.6.png'],
    ['but thence i learn and find the lesson true drugs poison him that so feil sick of you_0.7.png'],
    ['but thence i learn and find the lesson true drugs poison him that so feil sick of you_0.45.png'],
    ['but thence i learn and find the lesson true drugs poison him that so feil sick of you_0.55.png'],
    ['i am alone the villain of the earth and feel i am so most_0.3.png'],
    ['i am alone the villain of the earth and feel i am so most_0.4.png'],
    ['i am alone the villain of the earth and feel i am so most_0.6.png'],
    ['i am alone the villain of the earth and feel i am so most_0.45.png'],
    ['i am alone the villain of the earth and feel i am so most_0.55.png'],
    ['i am alone the villain of the earth and feel i am so most_0.65.png'],
    ['very simple text_0.3.png'],
    ['very simple text_0.4.png'],
    ['very simple text_0.5.png'],
    ['very simple text_0.6.png'],
    ['very simple text_0.7.png'],
    ['very simple text_0.45.png'],
    ['very simple text_0.55.png'],
    ['very simple text_0.png'],
    ['very simple text_1.png']
])

while True:
    for i in range(len(const_str_file_massive)):
        print('{}. '.format(i + 1), const_str_file_massive[i])
    print("-1.  EXIT")
    cmd = int(input("Choose a filename: ")) - 1
    if inside(cmd, -1, 22):
        c = const_str_file_massive[cmd]
        print(c[0])
        sleep(5)
    elif cmd == -2:
        break
    else:
        print("Вы ввели не правильное значение")

# x_, counts_ = x_picture_char_dictionary(const_string_x, const_str_path_to_input)
# a_ = standard_chars(const_string_alphabet)
#
# start_ = perf_counter()
# k_last_part(const_str_path_to_json, x_, counts_, a_, 0.7)
# end_ = perf_counter()
# print('\nTime of solution: ', end_ - start_)
