x = 1_000_000_000
y = 9_999_999_999
y = 1_040_000_021

for num in range(x, y+1):
    num_in_str = [int(i) for i in str(num)]
    print(num_in_str)

    q_even_digit = 0
    q_even_odd = 0
    for digit in num_in_str:
        # print(digit)
        if digit % 2 == 0:
            q_even_digit += 1
            # print(digit, 'четное')
        else:
            q_even_odd += 1
            # print(digit, 'нечетное')
    print(q_even_digit, 'четных,', q_even_odd, 'нечетных')
    print()

print()