s = input()

curLit = s[0]
cnt = 0

for i in s:
    if i == curLit:
        cnt += 1
    else:
        print(curLit, end=str(cnt))

        curLit = i
        cnt = 1

print(curLit, end=str(cnt))