a = [int(i) for i in input().split()]
b = []
x = len(a)
count = 1
if x > 2:
    for c in range(x):
        current_value = a[c]
        count += 1
        if count < x + 1:
            previous_value = a[c - 1]
            next_value = a[c + 1]
            sum = previous_value + next_value
            b += [sum]
        elif count == x + 1:
            previous_value = a[c - 1]
            next_value = a[0]
            sum = previous_value + next_value
            b += [sum]
elif x == 2:
    n = a[0]
    m = a[1]
    sum = m + m
    b += [sum]
    sum_2 = n + n
    b += [sum_2]
else:
    print(a[0])
print(*b)