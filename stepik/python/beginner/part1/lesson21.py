input = int(input())
left_var_1 = input // 1000
left_var_2 = input // 10000
left_1 = left_var_1 % 10
left_2 = left_var_1 // 100
left_3 = left_var_2 % 10
sum_left = left_1 + left_2 + left_3
right_var_1 = input % 1000
right_var_2 = input % 100
right_1 = right_var_1 % 10
right_2 = right_var_1 // 100
right_3 = right_var_2 // 10
sum_right = right_1 + right_2 + right_3
if sum_left == sum_right:
    print("Счастливый")
else:
    print("Обычный")