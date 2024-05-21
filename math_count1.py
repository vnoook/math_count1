import time
import datetime

# начальные данные 10-значных чисел
x = 1_000_000_000
# x = 1_111_111_101
# y = 9_999_999_999
# y = 1_000_010_129
y = 1_002_111_120

# вариант 1
time_start1 = time.time()

# словарь в котором буду сохранять количество вариантов
dict_of_variants = {}

# подсчёт количества чисел
for num in range(x, y+1):
    num_in_str = [int(i) for i in str(num)]
    # print(num_in_str)

    q_even_digit = 0
    q_odd_digit = 0
    for digit in num_in_str:
        # print(digit)
        if digit % 2 == 0:
            q_even_digit += 1
            # print(digit, 'четное')
        else:
            q_odd_digit += 1
            # print(digit, 'нечетное')

    flag_of_key = str(q_even_digit) + ' чет - ' + str(q_odd_digit) + ' нечет'
    # print(flag_of_key)

    # заполнение словаря отделений
    if dict_of_variants.get(flag_of_key) is None:
        dict_of_variants[flag_of_key] = 1
    else:
        dict_of_variants[flag_of_key] = dict_of_variants[flag_of_key] + 1

    # print(q_even_digit, 'четных,', q_odd_digit, 'нечетных')
    # print()

print(dict_of_variants)

time_stop1 = time.time()

time_format = str(datetime.timedelta(seconds = (time_stop1-time_start1)))
print()
print('.'*30 + 'закончено за', round(time_stop1-time_start1, 3), 'секунд')
print('.'*30 + 'закончено за', time_format)
