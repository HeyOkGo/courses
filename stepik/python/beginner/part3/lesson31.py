i = int(input())
start_point_1 = 0
start_point_2 = 0
for command in range(i):
    command = [str(i) for i in input().split()]
    if command[0] == 'север':
        start_point_2 += int(command[1])
    elif command[0] == 'восток':
        start_point_1 += int(command[1])
    elif command[0] == 'запад':
        start_point_1 -= int(command[1])
    elif command[0] == 'юг':
        start_point_2 -= int(command[1])
    else:
        print('by!')
print(start_point_1, start_point_2)