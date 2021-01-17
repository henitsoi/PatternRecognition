from func import k_last_part, x_picture_char_dictionary, standard_chars
from time import perf_counter
import numpy as np
from time import sleep


def inside(test_num, begin_range, end_range):
    return begin_range <= test_num <= end_range


const_str_path_massive = np.array(['data/input/', 'data/frequencies.json', 'data/alphabet'])


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

approximate_time = np.array(['27 sec', '95 sec', '144 sec'])

while True:
    for i in range(len(const_str_file_massive)):
        print('{}. '.format(i + 1), const_str_file_massive[i][0])
    print('0.  EXIT')
    cmd = int(input('Choose a filename: ')) - 1
    if inside(cmd, 0, 20):
        print(const_str_file_massive[cmd][0])
        noise_lvl = float(input('Choose a lvl of noise in range[0..1]: '))
        if inside(noise_lvl, 0.00, 1.00):
            if inside(cmd, 0, 5):
                print('The code is poorly optimized, therefore, the recognition time will be approximately: ',
                      approximate_time[2])
            elif inside(cmd, 6, 11):
                print('The code is poorly optimized, therefore, the recognition time will be approximately: ',
                      approximate_time[1])
            else:
                print('The code is poorly optimized, therefore, the recognition time will be approximately: ',
                      approximate_time[0])
            standard_ = standard_chars(const_str_path_massive[2])
            x_noisy_char, counts_ = x_picture_char_dictionary(const_str_file_massive[cmd][0], const_str_path_massive[0])
            start_ = perf_counter()
            k_last_part(const_str_path_massive[1], x_noisy_char, counts_, standard_, noise_lvl)
            end_ = perf_counter()
            print('\nTime of solution: ', end_ - start_)
            sleep(10)
        else:
            print('Incorrect number!!')
    elif cmd == -1:
        break
    else:
        print('Not correct value!!')
