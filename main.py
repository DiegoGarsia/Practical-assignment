# "1st program"

print((9 ** 0.5) * 5)

###############################################################################
# "2st program"

print((9.99 > 9.98) and (1000 != 1000.1))

###############################################################################
# "3st program"

a = 1234
b = 5678
First = a % 1000 / 10
Second = b % 1000 / 10

print('Сумма =', int(First) + int(Second))

###############################################################################
# "4st program"

float1 = 13.42
float2 = 42.13

number_left_float1 = (float1 * 100) // 100
left_float1 = int(number_left_float1)
# print('left_float1 =', left_float1)

number_right_float1 = (float1 * 100) % 100
right_float1 = int(number_right_float1)
# print('right_float1 =', right_float1)

number_left_float2 = (float2 * 100) // 100
left_float2 = int(number_left_float2)
# print('left_float2 =', left_float2)

number_right_float2 = (float2 * 100) % 100
right_float2 = int(number_right_float2)
# print('right_float2 =', right_float2)

if (left_float1 == right_float2) or (right_float1 == left_float2):
    print(True)
