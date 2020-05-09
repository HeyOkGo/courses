num = [int(i) for i in input().split()]
sum = []
for i in range(len(num)):
    if len(num) == 1:
        sum = num
        break
    if i == 0:
        sum = [num[-1] + num[i+1]]
    elif i == len(num)-1:
        sum += [num[0] + num[i-1]]
    else:
        sum += [num[i-1] + num[i+1]]
for i in range(len(sum)):
    print(sum[i], '', end='')